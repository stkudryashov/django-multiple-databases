from django.contrib import admin
from song.models import Song, Album


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'album']
    list_display_links = ['title']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration']
    list_display_links = ['title']
