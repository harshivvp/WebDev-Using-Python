from django.views import generic
from .models import Albums
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):

        return Albums.objects.all()


class DetailView(generic.DetailView):

    model = Albums
    template_name = 'polls/detail.html'

class AlbumCreate(CreateView):
    model = Albums
    fields = ['artist','title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Albums
    fields = ['artist','title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Albums
    success_url = reverse_lazy('polls:index')