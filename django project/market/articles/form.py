from django import forms
from . import models


class Creat_Article_form(forms.ModelForm):
    class Meta:
        model = models.Artic
        fields = ["title", "slug", "body", "image"]
