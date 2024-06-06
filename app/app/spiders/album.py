from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "album"


    def start_requests(self):
        artist_name = "daft punk"
        album_name = "discovery"

        urls = [
            "https://genius.com/albums/" + artist_name.replace(" ", "-") + "/" + album_name.replace(" ", "-")
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs={'artist':album_name.replace(" ", "-")})

    def parse(self, response, artist):
        for but in response.xpath('//a[contains(@href, "' + artist.capitalize() + '")]'):
            print("HERE1", but)
        print("HERE2", response)