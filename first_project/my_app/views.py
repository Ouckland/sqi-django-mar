from django.shortcuts import render, HttpResponse

# Create your views here.

def home(requests):
    return HttpResponse("Welcome to the page, user")