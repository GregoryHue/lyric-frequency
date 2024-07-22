from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from main.scraper.scraper import settings as my_settings
from main.scraper.scraper.spiders.album import AlbumSpider


class Command(BaseCommand):
    help = "Release spider"

    def add_arguments(self, parser):
        parser.add_argument("-O", "--output", type=str)

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        output = options["output"] if options["output"] else None

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(AlbumSpider, output)
        process.start()
