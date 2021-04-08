from django.shortcuts import render,HttpResponse


def home(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('About page')