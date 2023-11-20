from django.contrib import admin
from django.urls import include, path

import website.urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(website.urls)),
]
