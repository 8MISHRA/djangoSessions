from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You're at the home page of this project")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, world. You're at the about page of this project")

def contact(request):
    return HttpResponse("Hello, world. You're at the contact page of this project")
