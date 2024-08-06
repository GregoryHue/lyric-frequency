from django.http import HttpResponse
from django.template import loader
from main.django.models import Album
from main.django.serializers import AlbumSerializer
from django.core.management import call_command


def post(request):
    template = loader.get_template("../../web/templates/post.html")
    if request.method == "POST":
        if "artist" in request.POST and "album" in request.POST:
            artist_name = request.POST["artist"]
            album_name = request.POST["album"]
            print(artist_name, album_name)
            call_command("crawl", artist_name=artist_name, album_name=album_name)
            
            album = Album.objects.get(album_name=album_name, artist_name=artist_name)
            serializer = AlbumSerializer(album)
            print(serializer.data)
            # album_content = Album.objects.get(name=album_name, artist=artist_name)
            # serializer = AlbumSerializer(album_content)
            # print(serializer.data)
            # track_content = Track.objects.get(album=album_content)
            # serializer = TrackSerializer(track_content)
            # print(serializer.data)

    context = {
        "message": "hello",
    }
    return HttpResponse(template.render(context, request))
