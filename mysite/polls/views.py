from django.views import generic
from .models import Albums
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

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

class UserFormView(View):

    form_class = UserForm
    template_name = 'polls/registration-form.html'

    # blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    #Process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #This wont commit the data to the admin page yet.
            user = form.save(commit=False)

            #cleaned/normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #passwords aren't just normal texts. So.
            user.set_password(password)

            #Commit to the db on save()
            user.save()

            #return user objects if credentials are correct
            user = authenticate(username=username,password=password)

            #Check if the user value got back from db
            if user is not None:
                if user.is_active:
                    login(request,user) #now they're logged in.

                    #write something for them to know they're logged in or redirect them to home page
                    return redirect('polls:index')

        #If they didnt login. or account is disabled or banned.
        return render(request, self.template_name, {'form': form})

def search_titles(request):

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    albums = Albums.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html',{'albums':albums})