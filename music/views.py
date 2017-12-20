# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from music import models
from music.forms import CommentForm
from .models import Album, Song, Singer


def index(request):
    albums = Album.objects.all().order_by('album_date')[:6]
    singer=Singer.objects.all()
    song_list = Song.objects.all().order_by('song_point')[:15]
    lastest_song = Song.objects.all().order_by('song_date')[:15]
    context = {"albums" : albums, "song_list" : song_list , "lastest_song" : lastest_song, "singer": singer }

    return render(request, 'music/index.html', context)




def albumler_page(request):
    albums = Album.objects.all()
    song_list = Song.objects.all().order_by('song_point')[:15]
    lastest_song = Song.objects.all().order_by('song_date')[:15]
    context = {"albums" : albums, "song_list" : song_list, "lastest_song" : lastest_song}

    return render(request, 'music/albumler.html', context)


def album_page(request, album_id, album_title):
    print(album_id, album_title)
    song_list = Song.objects.all().order_by('song_point')[:15]
    lastest_song = Song.objects.all().order_by('song_date')[:15]
    album = get_object_or_404(Album, pk=album_id)
    context = {"album": album, "song_list" : song_list, "lastest_song" : lastest_song}
    return render(request, "music/album.html", context)







def songdetails_page(request, song_name , song_id):
    print(song_name , song_id)
    song = get_object_or_404(Song, pk=song_id)
    song_list = Song.objects.all().order_by('song_point')[:15]
    lastest_song = Song.objects.all().order_by('song_date')[:15]
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.song = song
        comment.save()
        return HttpResponseRedirect(song.get_absolute_url())

    context = {"song": song, "song_list" : song_list, "lastest_song" : lastest_song,"form":form}
    return render(request, "music/songdetails.html", context)


def sarkicilar_page(request):
    albums = Album.objects.all()
    song_list = Song.objects.all().order_by('song_point')[:15]
    singer = Album.objects.all()
    lastest_song = Song.objects.all().order_by('song_date')[:15]

    context = {"albums" : albums , "song_list" : song_list, "lastest_song" : lastest_song, "singer": singer}
    return render(request, 'music/sarkicilar.html', context)





def sarkicilardetails_page(request, singer_name , singer_id):
    print(singer_name , singer_id)
    albums = Album.objects.all()
    singer = get_object_or_404(Singer, pk=singer_id)
    song_list = Song.objects.all().order_by('song_point')[:15]
    lastest_song = Song.objects.all().order_by('song_date')[:15]
    context = {"albums" : albums , "singer": singer , "song_list" : song_list, "lastest_song" : lastest_song}
    return render(request, "music/sarkicilardetails.html", context)












def sarkilar(request):
    albums = Album.objects.all()
    song = Song.objects.all()
    song_list = Song.objects.all().order_by('song_point')[:15]
    lastest_song = Song.objects.all().order_by('song_date')[:15]
    context = {"albums" : albums , "song_list" : song_list, "lastest_song" : lastest_song, "song" : song }
    return render(request, 'music/sarkilar.html', context)


