from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome(requests):
    return HttpResponse("WELCOME TO MY APP")