import scrapy


class QuotesSpider(scrapy.Spider):
    name = "album"

    def start_requests(self):
        artist_name = "Des Rocs"
        album_name = "Dream Machine"

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
                cb_kwargs={
                    "artist_name": artist_name.replace(" ", "-"),
                    "album_name": album_name.replace(" ", "-"),
                },
            )

    def parse_song(self, response):
        for lyric in response.xpath(
            '//div[@class="Lyrics__Container-sc-1ynbvzw-1 kUgSbL"]//text()'
        ).extract():
            print(lyric)

    def parse_album(self, response, artist_name, album_name):
        for track in response.xpath(
            '//div[@class="column_layout-column_span column_layout-column_span--primary"]//a/@href'
        ).extract():
            yield scrapy.Request(
                url=track,
                callback=self.parse_song,
            )
        print("response:", response)
