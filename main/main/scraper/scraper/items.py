# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem

from main.web.models import Artist, Album, Track, Lyric


class ArtistItem(DjangoItem):
    django_model = Artist


class AlbumItem(DjangoItem):
    django_model = Album

    
class TrackItem(DjangoItem):
    django_model = Track

    
class LyricItem(DjangoItem):
    django_model = Lyric