"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from main.django.views import query_album, response_album, error, fetch_track
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from main.django.viewsets import AlbumViewSet

router = routers.DefaultRouter()
router.register(r"albums", AlbumViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", query_album.query_album, name="query_album"),
    path("query_album/", query_album.query_album, name="query_album"),
    path("response_album/", response_album.response_album, name="response_album"),
    path("fetch_track/<int:album_id>/<int:track_id>/", fetch_track.fetch_track, name="fetch_track"),
    path("api-view/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("__reload__/", include("django_browser_reload.urls")),
] 


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = error.error
handler500 = error.error