# from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
# from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
# from django.http import Http404
from .forms import AlbumForm,PictureForm
from .models import Album,Pictures
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


class PhotoIndexView(generic.ListView):

    model = Album
    context_object_name = 'albums'
    template_name = 'photoblog/index_list.html'


class CreateAlbumView(generic.CreateView):

    model = Album
    form_class = AlbumForm
    template_name = 'photoblog/create_album.html'
    success_url = reverse_lazy("photoblog:index_list")

    def post(self, request, *args, **kwargs):
        form = self.get_form(AlbumForm)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user.get_username()
            f.save()
            return self.form_valid(form)
        else:
            return HttpResponse("rip go back and try again")


class DeleteAlbumView(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('photoblog:index_list')


class PicturesDetailView(generic.ListView):

    model = Pictures
    context_object_name = 'pictures'
    template_name = 'photoblog/album_detail.html'

class CreatePicturesView(generic.CreateView):

    model = Pictures
    form_class = PictureForm
    context_object_name = 'pictures'
    template_name = 'photoblog/create_pic.html'
    success_url = reverse_lazy("photoblog:index_list")
