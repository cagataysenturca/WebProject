
from datetime import datetime
from django.db import models
from embed_video.fields import EmbedVideoField



class Album(models.Model):
    genre = models.ForeignKey('Genre')
    singer = models.ForeignKey('Singer')
    topic_author = models.ForeignKey('auth.User')
    album_title = models.CharField(max_length=1000)
    album_logo = models.ImageField(upload_to="music_imgs", blank=True)
    album_date = models.DateField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.album_title



class Song(models.Model):
    album = models.ForeignKey('Album')
    song_name=models.CharField(max_length=1000)
    video = models.CharField(max_length=1000)
    song_point = models.IntegerField()
    song_date = models.DateField(default=datetime.now(), blank=True)
    song_lyrics = models.TextField(blank=True)


    def __str__(self):
        return self.song_name



class Singer(models.Model):
    singer_foto = models.ImageField(upload_to="music_imgs", blank=True)
    singer_name = models.CharField(max_length=50)
    singer_life = models.TextField(blank=True)

    def __str__(self):
        return self.singer_name




class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre






