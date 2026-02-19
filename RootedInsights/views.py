from django.shortcuts import render

def home(request):
    # return HttpResponse("welcome to my blog")
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')