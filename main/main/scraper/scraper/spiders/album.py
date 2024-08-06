import scrapy
from scrapy.loader import ItemLoader
from main.scraper.scraper.items import AlbumItem, TrackItem
from scrapy.loader.processors import TakeFirst
import re


class AlbumSpider(scrapy.Spider):
    name = "album"
    full_lyrics = []
    song = []

    def start_requests(
        self,
    ):
        artist_name = re.sub(r"[^a-zA-Z ]", "", self.artist_name)
        album_name = re.sub(r"[^a-zA-Z ]", "", self.album_name)
        urls = [
            "https://genius.com/albums/"
            + artist_name.replace(" ", "-")
            + "/"
            + album_name.replace(" ", "-")
        ]
        print(urls)
        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_album,
            )

    def parse_song(self, response, artist_name, album_name):
        track_item = ItemLoader(item=TrackItem(), response=response)
        track_item.default_output_processor = TakeFirst()
        track_name = response.xpath(
            '//span[@class="SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj"]//text()'
        ).get()
        track_item.add_value("track_name", track_name)
        track_item.add_value("album", album_name)
        lyrics = ""
        for lyric in response.xpath(
            '//div[@class="Lyrics__Container-sc-1ynbvzw-1 kUgSbL"]//text()'
        ).extract():
            lyrics = lyrics + lyric.replace("\n", " ") + " "
        lyrics = re.sub(r"\[.*?\]", "", lyrics)
        track_item.add_value("lyrics", lyrics)
        yield track_item.load_item()

    def parse_album(self, response):
        album_item = ItemLoader(item=AlbumItem(), response=response)
        album_item.default_output_processor = TakeFirst()
        artist_name = response.xpath(
            '//div[@class="header_with_cover_art-primary_info"]//h2//a//text()'
        ).get()
        album_item.add_value("artist_name", artist_name)
        album_name = response.xpath(
            '//h1[@class="header_with_cover_art-primary_info-title header_with_cover_art-primary_info-title--white"]//text()'
        ).get()
        album_item.add_value("album_name", album_name)
        yield album_item.load_item()
        for track in response.xpath(
            '//div[@class="column_layout-column_span column_layout-column_span--primary"]//a/@href'
        ).extract():
            yield scrapy.Request(
                url=track,
                callback=self.parse_song,
                cb_kwargs={"artist_name": artist_name, "album_name": album_name},
            )
