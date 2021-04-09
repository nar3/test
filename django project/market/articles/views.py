from django.shortcuts import render, HttpResponse
from .models import Artic


def home(request):
    ar = Artic.objects.all().order_by("date")
    args = {"objects_in_artic_models": ar}
    return render(request, "articlehome.html", args)


def slug_pages(requesr, slug):
    return HttpResponse(slug)
