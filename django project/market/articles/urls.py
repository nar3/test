from django.urls import path
from . import views

app_name = "articles_urls_app"
urlpatterns = [
    path("", views.home, name="articles_home_page_redirect"),
    path("create/", views.create_article, name="article_create"),
    path("<slugname>/", views.slug_pages, name="articles_slug_page_redirect"),
]
