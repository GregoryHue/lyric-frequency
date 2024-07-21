import scrapy
from scrapy.loader import ItemLoader
from main.scraper.scraper.items import ArtistItem, AlbumItem, TrackItem, LyricItem


class AlbumSpider(scrapy.Spider):
    name = "album"
    full_lyrics = []
    song = []

    def start_requests(self):
        artist_name = "Daft Punk"
        album_name = "Discovery"

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
        track_item = ItemLoader(item=TrackItem(), response=response)
        track_name = response.xpath(
            '//span[@class="SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj"]//text()'
        ).get()
        track_item.add_value("name", track_name)
        track_item.add_value("album", album_name)
        track_item.add_value("artist", artist_name)
        yield track_item.load_item()
        i = 0
        for lyric in response.xpath(
            '//div[@class="Lyrics__Container-sc-1ynbvzw-1 kUgSbL"]//text()'
        ).extract():
            lyric_item = ItemLoader(item=LyricItem(), response=response)
            lyric_item.add_value("content", lyric)
            lyric_item.add_value("track", track_name)
            lyric_item.add_value("order", i)
            yield lyric_item.load_item()
            i = i + 1

    def parse_album(self, response):
        artist_item = ItemLoader(item=ArtistItem(), response=response)
        artist_name = response.xpath(
            '//div[@class="header_with_cover_art-primary_info"]//h2//a//text()'
        ).get()
        artist_item.add_value("name", artist_name)
        yield artist_item.load_item()
        album_name = response.xpath(
            '//h1[@class="header_with_cover_art-primary_info-title header_with_cover_art-primary_info-title--white"]//text()'
        ).get()
        album_item = ItemLoader(item=AlbumItem(), response=response)
        album_item.add_value("name", album_name)
        album_item.add_value("artist", artist_name)
        yield album_item.load_item()
        for track in response.xpath(
            '//div[@class="column_layout-column_span column_layout-column_span--primary"]//a/@href'
        ).extract():
            yield scrapy.Request(
                url=track,
                callback=self.parse_song,
                cb_kwargs={"artist_name": artist_name, "album_name": album_name},
            )
