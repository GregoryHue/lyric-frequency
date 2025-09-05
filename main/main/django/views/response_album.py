from django.http import HttpResponse
from django.template import loader
from main.django.models import Album, Track
from main.django.serializers import AlbumSerializer, TrackSerializer
from scrapy.crawler import CrawlerProcess
from main.scraper.scraper import settings as scrapy_settings
from main.scraper.scraper.spiders.album import AlbumSpider
from scrapy.settings import Settings
from multiprocessing.context import Process
from lyricsgenius import Genius
import os
import re


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
                print(" --- ", end="")
                access_token = os.environ.get("GENIUS_ACCESS_TOKEN")
                print(access_token)
                genius = Genius(access_token)
                album_content = genius.search_album(album_name, artist_name)
                album_content = album_content.to_dict()
                found_album_name = album_content["name"]
                found_artist_name = album_content["artist"]
                print(found_album_name, album_content)

                album = Album.objects.create(
                    album_name=found_album_name,
                    artist_name=found_artist_name,
                    album_image_url=album_content["cover_art_thumbnail_url"],
                    genius_url=album_content["url"],
                )

                album.save()

                for song in album_content["tracks"]:
                    print(song["song"]["title"])
                    lyrics = song["song"]["lyrics"].replace("\n", " ")
                    lyrics = re.sub(r"\[.*?\]", "", lyrics)
                    track = Track.objects.create(
                        track_name=song["song"]["title"],
                        lyrics=lyrics,
                        album=album,
                        track_order=song["number"],
                    )
                    track.save()

                # COMMENTING THIS BECAUSE WE'RE SWITCHING TO GENIUS API
                # print(" --- Crawling for data")
                # crawler_settings = Settings()
                # crawler_settings.setmodule(scrapy_settings)
                # process = Process(
                #     target=crawl, args=(crawler_settings, artist_name, album_name)
                # )
                # process.start()
                # process.join()
                # process.close()
                # print(" --- Finished crawling")

            try:
                album = Album.objects.get(
                    album_name__icontains=album_name, artist_name__icontains=artist_name
                )
                album_serializer = AlbumSerializer(album)

                # Checking for an 'Overall' lyric track
                does_overall_exist = False
                for track in album_serializer.data["tracks"]:
                    if track["track_name"] == "Overall occurrence":
                        does_overall_exist = True

                # Adding an 'Overall' lyric track
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
                    "error": None,
                }
            except Album.DoesNotExist:
                context = {
                    "data": None,
                    "error": "We could not find any artist with this album.",
                }
                template = loader.get_template("../../web/templates/error.html")
                return HttpResponse(template.render(context, request))
            except Exception as e:
                print(e)
                context = {
                    "data": None,
                    "error": e.message,
                }
                template = loader.get_template("../../web/templates/error.html")
                return HttpResponse(template.render(context, request))
        else:
            context = {
                "data": None,
                "error": "Empty request.",
            }
            template = loader.get_template("../../web/templates/error.html")
            return HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))
