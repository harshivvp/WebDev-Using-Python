from django.views import generic
from .models import Albums

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):

        return Albums.objects.all()


class DetailView(generic.DetailView):

    model = Albums
    template_name = 'polls/detail.html'