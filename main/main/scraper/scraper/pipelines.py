# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from asgiref.sync import sync_to_async
from django.db.utils import IntegrityError

from main.django.models import Album, Track


class ScraperPipeline(object):

    @sync_to_async
    def process_item(self, item, spider):
        if item.django_model == Album:
            try:
                item.save()
            except IntegrityError:
                pass
        if item.django_model == Track:
            try:
                if "track_name" in item:
                    item["album"] = Album.objects.get(album_name=item["album"])
                    item.save()
            except IntegrityError:
                pass
        return item
        
