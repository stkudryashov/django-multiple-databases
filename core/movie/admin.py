from django.contrib import admin
from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']
    list_display_links = ['title']
