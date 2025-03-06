from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(requests):
    return HttpResponse("Welcome to the homepage!")

def all_tasks(requests):
    return HttpResponse("What tasks do you want to perform? ")