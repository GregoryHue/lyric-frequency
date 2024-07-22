from django.http import HttpResponse
from django.template import loader



def get(request):
    template = loader.get_template("../../web/templates/get.html")
    context = {
    }
    return HttpResponse(template.render(context, request))