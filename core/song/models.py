from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    album = models.CharField(max_length=255, verbose_name='album')
    duration = models.PositiveIntegerField(verbose_name='duration')


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    duration = models.PositiveIntegerField(verbose_name='duration')

    class Meta:
        app_label = 'movie'
