from django.shortcuts import render, HttpResponse
from .models import Articles


def articles_list(request):
    articles = Articles.objects.all().order_by("date")
    args = {"articles": articles}
    return render(request, "articles/articleslist.html", args)
