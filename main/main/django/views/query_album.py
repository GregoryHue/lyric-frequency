from django.http import HttpResponse
from django.template import loader


def query_album(request):
    template = loader.get_template("../../web/templates/query_album.html")
    context = {}
    return HttpResponse(template.render(context, request))
