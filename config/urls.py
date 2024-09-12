from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from config.settings.base import env

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("src.apps.users.api.router")),
    path("api/v1/shared/", include("src.apps.shared.api.router")),
]


if env("DJANGO_ENV") == "local":
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
