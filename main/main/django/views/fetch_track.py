import json
import re
from django.http import HttpResponse
from main.django.models import Track
from main.django.serializers import TrackSerializer


def fetch_track(request, album_id, track_id):
    track = Track.objects.get(album_id=album_id, id=track_id)
    serializer = TrackSerializer(track)
    lyric_occurrence = {}

    if len(serializer.data["lyrics"]) > 0:
        # Removing special characters
        print("Removing special characters")
        lyrics = serializer.data["lyrics"]
        lyrics = re.sub(r"[^a-zA-Z0-9 \'\-]", "", lyrics)
        lyrics = re.sub(r"[\-]", " ", lyrics).strip()
        each_lyrics = lyrics.split(" ")

        # Creating a dictionnary, later transformed into a DataFrame
        print("Creating a dictionnary, later transformed into a DataFrame")
        for lyric in each_lyrics:
            lyric = lyric.lower()
            if lyric != "":
                if lyric in lyric_occurrence:
                    lyric_occurrence[lyric] = lyric_occurrence[lyric] + 1
                else:
                    lyric_occurrence[lyric] = 1
        print(json.dumps(lyric_occurrence))
        return HttpResponse(json.dumps(lyric_occurrence), request)
    
    return HttpResponse("<div class=\"text-white ml-12 text-xl\">No lyrics for: " + serializer.data["track_name"] + "</div>", request)
