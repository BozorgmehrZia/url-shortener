from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from urlshortener.models import Shortener
from urlshortener.utils import get_random_string
from datetime import datetime

def get_short_from_long(request, long_url):
    url = Shortener.objects.filter(long_url=long_url)
    if not url.exists():
        url = Shortener.objects.create(long_url=long_url, short_url=get_random_string(), created=datetime.now())
        return HttpResponse(url.short_url)
    return HttpResponse(url.first().short_url)


def get_long_from_short(request, short_url):
    url = Shortener.objects.filter(short_url=short_url)
    return redirect("https://" + url.first().long_url)
