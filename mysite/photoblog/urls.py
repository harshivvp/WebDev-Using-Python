from django.urls import path
from . import views

app_name = 'photoblog'

urlpatterns = [
        path('', views.PhotoIndexView.as_view() ,name='index_list'),
        path('create_album/', views.CreateAlbumView.as_view(), name='create_album'),
        path('<int:pk>/album_delete/', views.DeleteAlbumView.as_view(), name='delete_album'),
        path('<int:pk>/picture_detail/', views.PicturesDetailView.as_view(), name='picture_detail'),
        path('<int:pk>/create_pictures/', views.CreatePicturesView.as_view(), name='create_picture'),
]



