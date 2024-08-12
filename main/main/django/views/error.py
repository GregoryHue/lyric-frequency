from django.http import HttpResponse
from django.template import loader


def error(request, *exception):
    template = loader.get_template("../../web/templates/error.html")
    context = {"message": exception}
    return HttpResponse(template.render(context, request))
