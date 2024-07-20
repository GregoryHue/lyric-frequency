# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from asgiref.sync import sync_to_async


class ScraperPipeline(object):
    @sync_to_async
    def process_item(self, item, spider):
        print(item)
        item.save()
        return item
