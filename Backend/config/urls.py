from django.contrib import admin
from django.urls import path, include
from rooms import views as room_views
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
]