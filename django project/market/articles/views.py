from django import http
from django.http import request
from django.shortcuts import render, HttpResponse
from .models import Artic


def home(request):
    ar = Artic.objects.all().order_by("-date")
    args = {"objects_in_artic_models": ar}
    return render(request, "articlehome.html", args)


def slug_pages(request, slugname):
    ar = Artic.objects.get(slug=slugname)
    args = {"slug_in_article_models": ar}
    return render(request, "artile_by_slug.html", args)
