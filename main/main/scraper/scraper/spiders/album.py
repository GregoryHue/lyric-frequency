import scrapy
from scrapy.loader import ItemLoader
from main.scraper.scraper.items import ScraperItem
from itemloaders.processors import TakeFirst


class AlbumSpider(scrapy.Spider):
    name = "album"
    full_lyrics = []
    song = []

    def start_requests(self):
        artist_name = "Des Rocs"
        album_name = "Dream Machine"

        urls = [
            "https://genius.com/albums/"
            + artist_name.replace(" ", "-")
            + "/"
            + album_name.replace(" ", "-")
        ]
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_album,
            )

    def parse_song(self, response, artist_name, album_name):
        item_to_yield = ItemLoader(item=ScraperItem(), response=response)
        item_to_yield.default_output_processor = TakeFirst()
        item_to_yield.add_value("name", artist_name)
        # track_name = response.xpath(
        #     '//span[@class="SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj"]//text()'
        # ).get()
        # i = 0
        # for lyric in response.xpath(
        #     '//div[@class="Lyrics__Container-sc-1ynbvzw-1 kUgSbL"]//text()'
        # ).extract():
        #     item_to_yield.add_value('name', artist_name)
        #     i = i + 1
        yield item_to_yield.load_item()

    def parse_album(self, response):
        artist_name = response.xpath(
            '//div[@class="header_with_cover_art-primary_info"]//h2//a//text()'
        ).get()
        album_name = response.xpath(
            '//h1[@class="header_with_cover_art-primary_info-title header_with_cover_art-primary_info-title--white"]//text()'
        ).get()
        for track in response.xpath(
            '//div[@class="column_layout-column_span column_layout-column_span--primary"]//a/@href'
        ).extract():
            yield scrapy.Request(
                url=track,
                callback=self.parse_song,
                cb_kwargs={"artist_name": artist_name, "album_name": album_name},
            )
