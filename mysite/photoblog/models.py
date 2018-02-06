from django.db import models
from django.utils import timezone


class Album(models.Model):
    user = models.CharField(max_length=25)
    album_title = models.CharField(max_length=30)
    album_logo = models.FileField(default='')
    slug = models.SlugField(null=True, blank=True)
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.album_title

class Pictures(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    pictures = models.FileField(default='')
    pic_title = models. CharField(max_length=100)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.pic_title