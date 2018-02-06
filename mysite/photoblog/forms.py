from django import forms
from django.contrib.auth.models import User

from .models import Album,Pictures


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_title', 'album_logo','view_count','publish_date']

class PictureForm(forms.ModelForm):

    class Meta:
        model = Pictures
        fields = ['album', 'pictures', 'pic_title', 'publish_date']