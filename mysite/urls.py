
from django.contrib import admin
from django.urls import path, include
from . import url_handlers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", url_handlers.index_handler),
    path("moviebook/", include("moviebook.urls")),
]
