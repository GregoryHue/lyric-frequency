from django.http import HttpResponse
from django.template import loader

from main.django.models import Album
from main.django.serializers import AlbumSerializer


def query_album(request):
    template = loader.get_template("../../web/templates/query_album.html")
    album_examples = Album.objects.all().order_by("-id")[:3]
    album_serializer = AlbumSerializer(album_examples, many=True)
    context = {"data": album_serializer.data}
    return HttpResponse(template.render(context, request))
