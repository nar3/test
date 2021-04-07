from django.shortcuts import render,HttpResponse

def about(request):
    #return HttpResponse("Here is about page")
    return render(request,'about.html')

def home(request):
    #return HttpResponse("Here is Home page")
    return render(request,'home.html')

def articles_list(request):
    return render(request,'')