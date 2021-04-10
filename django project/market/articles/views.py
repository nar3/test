from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Artic
from . import form


def home(request):
    ar = Artic.objects.all().order_by("-date")
    args = {"objects_in_artic_models": ar}
    return render(request, "articlehome.html", args)


@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == "POST":
        create_article_forms = form.Creat_Article_form(request.POST, request.FILES)
        if create_article_forms.is_valid:
            create_article_forms.save()
            return redirect("articles_urls_app:articles_home_page_redirect")
    else:
        create_article_forms = form.Creat_Article_form()
        args = {"create_article_forms": create_article_forms}
    return render(request, "create_article.html", args)


def slug_pages(request, slugname):
    ar = Artic.objects.get(slug=slugname)
    args = {"slug_in_article_models": ar}
    return render(request, "artile_by_slug.html", args)
