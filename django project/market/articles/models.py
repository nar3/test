from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH


class Artic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title

    def abstract(self):
        return self.body[:50] + " ..."
