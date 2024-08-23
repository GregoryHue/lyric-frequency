from django.http import HttpResponse
from django.template import loader
from main.django.models import Album
from main.django.serializers import AlbumSerializer
from scrapy.crawler import CrawlerProcess
from main.scraper.scraper import settings as scrapy_settings
from main.scraper.scraper.spiders.album import AlbumSpider
from scrapy.settings import Settings
from multiprocessing.context import Process


def crawl(crawler_settings, artist_name, album_name):
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(AlbumSpider, artist_name=artist_name, album_name=album_name)
    crawler_process.start(install_signal_handlers=False)


def response_album(request):
    template = loader.get_template("../../web/templates/response_album.html")
    if request.method == "GET":
        if "artist" in request.GET and "album" in request.GET:
            # Reading user inputs
            print("Reading user inputs")
            artist_name = request.GET["artist"]
            album_name = request.GET["album"]

            # Crawling for data if it isn't already stored
            print("Crawling for data if it isn't already stored")
            if False:
                crawler_settings = Settings()
                crawler_settings.setmodule(scrapy_settings)
                process = Process(
                    target=crawl, args=(crawler_settings, artist_name, album_name)
                )
                process.start()
                process.join()
                process.close()
                print("close()")

            album = Album.objects.get(album_name=album_name, artist_name=artist_name)
            serializer = AlbumSerializer(album)
            track_index = 0

            # Adding an 'Overall' graph
            # print("Adding an 'Overall' graph")
            # general_lyrics = " ".join(
            #     [track["lyrics"] for track in serializer.data["tracks"]]
            # )
            # serializer.data["tracks"].insert(
            #     0,
            #     {
            #         "track_name": "Overall occurrence of each word in the whole album",
            #         "lyrics": general_lyrics,
            #         "album": serializer.data["tracks"][track_index]["album"],
            #     },
            # )

            # Reading each tracks
            print("Reading each tracks")
            

                # serializer.data["tracks"][track_index]["graph_data"] = lyric_occurrence
                # track_index = track_index + 1

            context = {
                "data": serializer.data,
            }
        else:
            context = {}

    print("HttpResponse(template.render(context, request))")
    return HttpResponse(template.render(context, request))

