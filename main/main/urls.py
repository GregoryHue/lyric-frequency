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
from main.django.views import get, post, error
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from main.django.viewsets import AlbumViewSet

router = routers.DefaultRouter()
router.register(r"albums", AlbumViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get.get, name="get"),
    path("get/", get.get, name="get"),
    path("post/", post.post, name="post"),
    path("api-view/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = error.error
handler500 = error.error