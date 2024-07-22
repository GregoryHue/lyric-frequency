from django.http import HttpResponse
from django.template import loader


def post(request):
    template = loader.get_template("../../web/templates/post.html")
    if request.method == "POST":
        if "artist" in request.POST and "album" in request.POST:
            artist = request.POST["artist"]
            album = request.POST["album"]
            
    context = {
        "message": "hello",
    }
    return HttpResponse(template.render(context, request))
