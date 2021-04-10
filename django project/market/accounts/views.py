from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_def(request):
    if request.method == "POST":
        form0 = UserCreationForm(request.POST)
        if form0.is_valid():
            form0.save()
            # login
            return redirect("articles_urls_app:articles_home_page_redirect")
    else:
        form0 = UserCreationForm()
    return render(request, "signup.html", {"form1": form0})


def login_def(request):
    if request.method == "POST":
        form0 = AuthenticationForm(data=request.POST)
        if form0.is_valid():
            user_get = form0.get_user()
            login(request, user_get)
            if "next_key" in request.POST:
                return redirect(request.POST.get("next_key"))
            else:
                return redirect("articles_urls_app:articles_home_page_redirect")
    else:
        form0 = AuthenticationForm()
    return render(request, "login.html", {"form1": form0})


def logout_def(request):
    if request.method == "POST":
        logout(request)
        return redirect("articles_urls_app:articles_home_page_redirect")