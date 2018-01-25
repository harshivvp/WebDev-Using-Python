from django.db import models

class Albums(models.Model):

    #Columns in DB
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + " - " + self.artist

class Songs(models.Model):

    #Needs to be associated with an album. part of one.
    album = models.ForeignKey(Albums,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + " - " + self.file_type