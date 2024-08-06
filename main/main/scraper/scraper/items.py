# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from main.django.models import Album, Track


class AlbumItem(DjangoItem):
    django_model = Album


class TrackItem(DjangoItem):
    django_model = Track
