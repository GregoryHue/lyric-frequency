import re
from django.http import HttpResponse
from django.template import loader
import pandas as pd
import plotly
from main.django.models import Album
from main.django.serializers import AlbumSerializer
from dataclasses import make_dataclass
import plotly.express as px
from django.core.management import call_command


def post(request):
    template = loader.get_template("../../web/templates/post.html")
    if request.method == "POST":
        if "artist" in request.POST and "album" in request.POST:
            artist_name = request.POST["artist"]
            album_name = request.POST["album"]
            call_command("crawl", artist_name=artist_name, album_name=album_name)

            album = Album.objects.get(album_name=album_name, artist_name=artist_name)
            serializer = AlbumSerializer(album)
            track_index = 0
            for track in serializer.data["tracks"]:
                lyric_occurrence = {}
                lyrics = track["lyrics"]
                lyrics = re.sub(r"[\?\,\.\(\)]", "", lyrics)
                lyrics = re.sub(r"[\-]", " ", lyrics).strip()
                each_lyrics = lyrics.split(" ")

                for lyric in each_lyrics:
                    lyric = lyric.lower()
                    if lyric != "":
                        if lyric in lyric_occurrence:
                            lyric_occurrence[lyric] = lyric_occurrence[lyric] + 1
                        else:
                            lyric_occurrence[lyric] = 1

                if lyric_occurrence != {}:
                    Point = make_dataclass(
                        "Point", [("word", str), ("occurrence", int)]
                    )
                    df = pd.DataFrame(
                        [
                            Point(word, lyric_occurrence[word])
                            for word in lyric_occurrence
                        ]
                    )
                    filtered_df = df[df["occurrence"] > 1]
                    filtered_df.sort_values(by=["occurrence"], ascending=[True], inplace=True)
                    fig = px.bar(
                        filtered_df,
                        title=track["track_name"],
                        x="occurrence",
                        y="word",
                        color_discrete_sequence=px.colors.sequential.RdBu,
                    )
                    graph_div = plotly.offline.plot(
                        fig, auto_open=False, output_type="div"
                    )

                    serializer.data["tracks"][track_index]["graph"] = graph_div
                    track_index = track_index + 1

    context = {
        "data": serializer.data,
    }
    return HttpResponse(template.render(context, request))
