from django.http import HttpResponse
from django.template import loader
from main.django.models import Album, Track
from main.django.serializers import AlbumSerializer, TrackSerializer
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
            artist_name = request.GET["artist"]
            album_name = request.GET["album"]

            # Crawling for data if it isn't already stored
            if not Album.objects.filter(
                album_name=album_name, artist_name=artist_name
            ).exists():
                crawler_settings = Settings()
                crawler_settings.setmodule(scrapy_settings)
                process = Process(
                    target=crawl, args=(crawler_settings, artist_name, album_name)
                )
                process.start()
                process.join()
                process.close()

            album = Album.objects.get(album_name=album_name, artist_name=artist_name)
            album_serializer = AlbumSerializer(album)

            #Checking for an 'Overall' lyric track
            does_overall_exist = False
            for track in album_serializer.data["tracks"]:
                if track["track_name"] == "Overall occurrence":
                    does_overall_exist = True

            #Adding an 'Overall' lyric track
            if not does_overall_exist:
                general_lyrics = " ".join(
                    [track["lyrics"] for track in album_serializer.data["tracks"]]
                )
                new_overall_track = Track.objects.create(
                    track_name="Overall occurrence",
                    lyrics=general_lyrics,
                    album_id=album_serializer.data["id"],
                    track_order=0,
                )
                new_overall_track.save()
                track_serializer = TrackSerializer(new_overall_track)
                album_serializer.data["tracks"].insert(0, track_serializer.data)

            context = {
                "data": album_serializer.data,
            }
        else:
            context = {}
    return HttpResponse(template.render(context, request))
