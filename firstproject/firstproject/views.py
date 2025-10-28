from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World! You are at my first Django project home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is the about page of my first Django project about page.")

def contact(request):
    return HttpResponse("This is the contact page of my first Django project contact page.")

