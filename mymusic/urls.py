from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static

from music import views
from mymusic import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),




    url(r'^albumler/', views.albumler_page, name='albumler'),
    url(r'^album/(?P<album_title>.+)/(?P<album_id>[0-9]+)', views.album_page, name='album'),



    url(r'^songdetails/(?P<song_name>.+)/(?P<song_id>[0-9]+)' , views.songdetails_page, name='songdetails'),




    url(r'^sarkicilar/', views.sarkicilar_page, name='sarkicilar'),
    url(r'^sarkicilardetails/(?P<singer_name>.+)/(?P<singer_id>[0-9]+)' , views.sarkicilardetails_page, name='sarkicilardetails'),


    url(r'^sarkilar/', views.sarkilar, name='sarkilar'),

    url(r'^roportaj/', views.roportaj, name='roportaj'),

    url(r'^/(?P<roportaj_id>[0-9]+)' , views.roportajdetails_page, name='roportajdetails'),



]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

