from django.shortcuts import render

# Create your views here.

def home(request):
    v="this is my home"
    return render(request,'home.html',context={'data':v})

def about(request):
    data="this is about"
    return render(request,'about.html',context={'data':data})
