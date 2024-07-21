# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from asgiref.sync import sync_to_async
from django.db.utils import IntegrityError

from main.web.models import Artist, Album, Track, Lyric


class ScraperPipeline(object):
    @sync_to_async
    def process_item(self, item, spider):
        if item.django_model == Artist:
            try:
                item.save()
            except(IntegrityError):
                pass
        if item.django_model == Album:
            item['artist'] = Artist.objects.get(name=item['artist'])
            try:
                item.save()
            except(IntegrityError):
                pass
        if item.django_model == Track:
            try:
                item['album'] = Album.objects.get(name=item['album'])
                item['artist'] = Artist.objects.get(name=item['artist'])
                item.save()
            except(IntegrityError):
                pass
        if item.django_model == Lyric:
            item['track'] = Track.objects.get(name=item['track'])
            try:
                item.save()
            except(IntegrityError):
                pass
        return item
