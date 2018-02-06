from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.utils.decorators import method_decorator

from .forms import UserForm, SongForm
from .models import Album, Song


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class AlbumIndex(generic.ListView):

    try:
        if Album.objects.all() is not None:

            template_name = 'music_gcb/index.html'
            context_object_name = 'albums'

            def get_queryset(self):
                return Album.objects.all()
    except ObjectDoesNotExist:
        raise Http404(":| rip")


class AlbumDetail(generic.DetailView):

    model = Album
    template_name = 'music_gcb/detail.html'


    @method_decorator(login_required)
    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['album_title'] = Album.objects.all()
        return context


class AlbumDelete(generic.DeleteView):

    model = Album
    success_url = reverse_lazy('music_gcb:index')


class SongDelete(generic.DeleteView):

    model = Song
    success_url = reverse_lazy('music_gcb:detail.html')


class CreateAlbum(generic.CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'music_gcb/create_album.html'
    success_url = reverse_lazy('music_gcb:index')
    context_object_name = 'albums'


class CreateSong(generic.CreateView):

    model = Song
    fields = ['album', 'song_title', 'audio_file', 'is_favorite']
    template_name = 'music_gcb/create_song.html'
    success_url = reverse_lazy("music_gcb:detail")


    def get_context_data(self, **kwargs):
        context = super(CreateSong, self).get_context_data(**kwargs)
        album = Album.objects.get(id=self.kwargs.get(self.pk_url_kwarg))
        context.update({'album': album})
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form(SongForm)
        post = Song()
        if form.is_valid():
            f = form.save(commit=False)
            f.song_title = post.song_title
            f.audio_file = post.audio_file
            f.is_favorite = post.is_favorite
            f.save()
        return self.form_valid(form)

        # def post(self, request, *args, **kwargs):
        #     post = self.get_object()
        #     form = CommentForm(request.POST)
        #     if form.is_valid():
        #         f = form.save(commit=False)
        #         f.post_id = post.id
        #         f.ip_address = self.get_client_ip(self.request)
        #         f.save()
        #         form.send_email()
        #         messages.add_message(self.request, messages.SUCCESS, 'Comment submitted. Thanks!')
        #         return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))

    # def create_song(request, album_id):
    #     form = SongForm(request.POST or None, request.FILES or None)
    #     album = get_object_or_404(Album, pk=album_id)
    #     if form.is_valid():
    #         albums_songs = album.song_set.all()
    #         for s in albums_songs:
    #             if s.song_title == form.cleaned_data.get("song_title"):
    #                 context = {
    #                     'album': album,
    #                     'form': form,
    #                     'error_message': 'You already added that song',
    #                 }
    #                 return render(request, 'music_gcb/create_song.html', context)
    #         song = form.save(commit=False)
    #         song.album = album
    #         song.audio_file = request.FILES['audio_file']
    #         file_type = song.audio_file.url.split('.')[-1]
    #         file_type = file_type.lower()
    #         if file_type not in AUDIO_FILE_TYPES:
    #             context = {
    #                 'album': album,
    #                 'form': form,
    #                 'error_message': 'Audio file must be WAV, MP3, or OGG',
    #             }
    #             return render(request, 'music_gcb/create_song.html', context)
    #         song.save()
    #         return render(request, 'music_gcb/detail.html', {'album': album})
    #     context = {
    #         'album': album,
    #         'form': form,
    #     }
    #     return render(request, 'music_gcb/create_song.html', context)

#
# def delete_album(request, album_id):
#     album = Album.objects.get(pk=album_id)
#     album.delete()
#     albums = Album.objects.filter(user=request.user)
#     return render(request, 'music_gcb/index.html', {'albums': albums})
#
#
# def delete_song(request, album_id, song_id):
#     album = get_object_or_404(Album, pk=album_id)
#     song = Song.objects.get(pk=song_id)
#     song.delete()
#     return render(request, 'music_gcb/detail.html', {'album': album})


#
#
# def detail(request, album_id):
#     if not request.user.is_authenticated:
#         return render(request, 'music_gcb/login.html')
#     else:
#         user = request.user
#         album = get_object_or_404(Album, pk=album_id)
#         return render(request, 'music_gcb/detail.html', {'album': album, 'user': user})


def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, ObjectDoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, ObjectDoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



#
# def index(request):
#     if not request.user.is_authenticated:
#         return render(request, 'music_gcb/login.html')
#     else:
#         albums = Album.objects.filter(user=request.user)
#         song_results = Song.objects.all()
#         query = request.GET.get("q")
#         if query:
#             albums = albums.filter(
#                 Q(album_title__icontains=query) |
#                 Q(artist__icontains=query)
#             ).distinct()
#             song_results = song_results.filter(
#                 Q(song_title__icontains=query)
#             ).distinct()
#             return render(request, 'music_gcb/index.html', {
#                 'albums': albums,
#                 'songs': song_results,
#             })
#         else:
#             return render(request, 'music_gcb/index.html', {'albums': albums})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music_gcb/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music_gcb/index.html', {'albums': albums})
            else:
                return render(request, 'music_gcb/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music_gcb/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music_gcb/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music_gcb/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music_gcb/register.html', context)


def songs(request, filter_by):
    # if not request.user.is_authenticated:
    #     return render(request, 'music_gcb/login.html')
    # else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except ObjectDoesNotExist:
            users_songs = []
        return render(request, 'music_gcb/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })
