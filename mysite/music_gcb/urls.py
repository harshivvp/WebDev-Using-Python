from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'music_gcb'

urlpatterns = [

    path('', views.AlbumIndex.as_view(), name='index'),
    path('<int:pk>/', views.AlbumDetail.as_view(), name='detail'),
    path('create_album/', views.CreateAlbum.as_view(), name='create_album'),
    path('<int:pk>/delete_album/', views.AlbumDelete.as_view(), name='delete_album'),
    path('<int:pk>/create_song/', views.CreateSong.as_view(), name='create_song'),
    # path(r'<int:pk>/delete_song/(?P<song_id>[0-9]+)/', views.SongDelete.as_view(), name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]
