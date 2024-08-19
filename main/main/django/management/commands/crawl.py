"""from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from main.scraper.scraper import settings as my_settings
from main.scraper.scraper.spiders.album import AlbumSpider
from multiprocessing.context import Process


def crawl(crawler_settings, artist_name, album_name):
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(AlbumSpider, artist_name=artist_name, album_name=album_name)
    process.start(install_signal_handlers=False)


class Command(BaseCommand):
    help = "Release spider"

    def add_arguments(self, parser):
        parser.add_argument("-S", "--artist_name", type=str)
        parser.add_argument("-A", "--album_name", type=str)

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        if options["artist_name"] is not None and options["album_name"] is not None:
            artist_name = options["artist_name"]
            album_name = options["album_name"]

            process = Process(
                target=crawl, args=(crawler_settings, artist_name, album_name)
            )
            process.start()
            process.join()
        else:
            raise Exception("Enter a valid artist name and album name.")
"""
