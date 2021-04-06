from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    rating = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='rating')
    duration = models.PositiveIntegerField(verbose_name='duration')
