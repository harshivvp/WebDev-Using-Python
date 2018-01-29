from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('albums/add/$', views.AlbumCreate.as_view(), name='albums-add'),
    path('albums/<int:pk>/$', views.AlbumUpdate.as_view(), name='albums-upd'),
    path('albums/<int:pk>/delete/$', views.AlbumDelete.as_view(), name='albums-del'),
]
