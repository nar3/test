from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):
    if request.method == "POST":
        form0 = UserCreationForm(request.POST)
        if form0.is_valid():
            form0.save()
            # login
            return redirect("articles_urls_app:articles_home_page_redirect")
    else:
        form0 = UserCreationForm()
    return render(request, "signup.html", {"form1": form0})


def login(request):
    if request.method == "POST":
        form0 = AuthenticationForm(data=request.POST)
        if form0.is_valid:
            return redirect("articles_urls_app:articles_home_page_redirect")
    else:
        form0 = AuthenticationForm()
    return render(request, "login.html", {"form1": form0})
