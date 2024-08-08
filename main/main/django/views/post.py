import re
from django.http import HttpResponse
from django.template import loader
from main.django.models import Album
from main.django.serializers import AlbumSerializer
from django.core.management import call_command

from main.django.utils import make_graph


def post(request):
    template = loader.get_template("../../web/templates/post.html")
    if request.method == "POST":
        if "artist" in request.POST and "album" in request.POST:
            # Reading user inputs
            artist_name = request.POST["artist"]
            album_name = request.POST["album"]

            # Crawling for data if it isn't already stored
            if not Album.objects.filter(
                album_name=album_name, artist_name=artist_name
            ).exists():
                call_command("crawl", artist_name=artist_name, album_name=album_name)

            album = Album.objects.get(album_name=album_name, artist_name=artist_name)
            serializer = AlbumSerializer(album)
            track_index = 0

            # Adding a 'Overall' graph
            general_lyrics = " ".join(
                [track["lyrics"] for track in serializer.data["tracks"]]
            )
            serializer.data["tracks"].insert(
                0,
                {
                    "track_name": "Overall occurrence of each word in the whole album",
                    "lyrics": general_lyrics,
                    "album": serializer.data["tracks"][track_index]["album"],
                },
            )

            # Reading each tracks
            for track in serializer.data["tracks"]:
                lyric_occurrence = {}

                # Removing special characters
                lyrics = track["lyrics"]
                lyrics = re.sub(r"[^a-zA-Z0-9 \'\-]", "", lyrics)
                lyrics = re.sub(r"[\-]", " ", lyrics).strip()
                each_lyrics = lyrics.split(" ")

                # Creating a dictionnary, later transformed into a DataFrame
                for lyric in each_lyrics:
                    lyric = lyric.lower()
                    if lyric != "":
                        if lyric in lyric_occurrence:
                            lyric_occurrence[lyric] = lyric_occurrence[lyric] + 1
                        else:
                            lyric_occurrence[lyric] = 1

                # Generating a graph
                if lyric_occurrence != {}:
                    serializer.data["tracks"][track_index]["graph"] = make_graph(
                        lyric_occurrence, track
                    )
                    track_index = track_index + 1

    context = {
        "data": serializer.data,
    }
    return HttpResponse(template.render(context, request))
