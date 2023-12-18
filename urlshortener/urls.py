from django.urls import path

from urlshortener import views

urlpatterns = [
    path("long-url/<long_url>/", views.get_short_from_long, name ="get_short_from_long"),
    path("short-url/<short_url>/", views.get_long_from_short, name ="get_long_from_short"),
]