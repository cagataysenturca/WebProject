from __future__ import unicode_literals

from django.contrib import admin
from .models import Album, Song, Singer, Genre

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Genre)
