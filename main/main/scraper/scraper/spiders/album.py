import scrapy
from scrapy.loader import ItemLoader
from main.scraper.scraper.items import AlbumItem, TrackItem
from itemloaders.processors import TakeFirst
import re


class AlbumSpider(scrapy.Spider):
    name = "album"
    full_lyrics = []
    song = []

    def start_requests(
        self,
    ):
        print(" --- Starting spider")
        # Reading user input and removing special characters
        artist_name = re.sub(r"[^a-zA-Z ]", "", self.artist_name)
        album_name = re.sub(r"[^a-zA-Z ]", "", self.album_name)
        urls = [
            "https://genius.com/albums/"
            + artist_name.replace(" ", "-")
            + "/"
            + album_name.replace(" ", "-")
        ]
        # Fetching lyrics from Genius.com
        for url in urls:
            print(" --- Url:", url)
            yield scrapy.Request(
                url=url,
                callback=self.parse_album,
                cb_kwargs={"genius_url": url},
            )

    def parse_song(self, response, album_name, i):
        print(1)
        track_item = ItemLoader(item=TrackItem())
        print(2)
        track_item.default_output_processor = TakeFirst()
        print(3)
        track_name = response.xpath(
            '//span[contains(@class, "SongHeader-desktop__HiddenMask")]//text()'
        ).get()
        print(4)
        track_item.add_value("track_order", i)
        print(5)
        track_item.add_value("track_name", track_name)
        print(" --- Track name:", track_name)
        track_item.add_value("album", album_name)
        lyrics = ""
        for lyric in response.xpath(
            '//div[contains(@class, "Lyrics__Container")]//text()'
        ).extract():
            lyrics = lyrics + lyric.replace("\n", " ") + " "
        # Ignoring lines such as: [Verse 1]
        lyrics = re.sub(r"\[.*?\]", "", lyrics)
        track_item.add_value("lyrics", lyrics)
        yield track_item.load_item()

    def parse_album(self, response, genius_url):
        try:
            album_item = ItemLoader(item=AlbumItem())
            album_item.default_output_processor = TakeFirst()
            album_item.add_value("genius_url", genius_url)
            album_image = response.xpath(
                '//div[@class="header_with_cover_art-inner column_layout"]//img/@src'
            ).extract_first()
            album_item.add_value("album_image_url", album_image)
            artist_name = response.xpath(
                '//div[@class="header_with_cover_art-primary_info"]//h2//a//text()'
            ).get()
            album_item.add_value("artist_name", artist_name)
            album_name = response.xpath(
                '//h1[@class="header_with_cover_art-primary_info-title header_with_cover_art-primary_info-title--white"]//text()'
            ).get()
            album_item.add_value("album_name", album_name)
            print(" --- Album name:", album_name)
            yield album_item.load_item()
            i = 0
            for track in response.xpath(
                '//div[@class="column_layout-column_span column_layout-column_span--primary"]//a[@class="u-display_block"]/@href'
            ).extract():
                i = i + 1
                yield scrapy.Request(
                    url=track,
                    callback=self.parse_song,
                    cb_kwargs={"album_name": album_name, "i": i},
                )

        except Exception as e:
            print("Exception:", e)
