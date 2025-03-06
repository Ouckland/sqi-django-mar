from django.shortcuts import render, HttpResponse

# Create your views here.

def menu(request):
    return HttpResponse("We can offer you: \n Rice with coleslaw\n Beans\n Pizza")

def contact(request):
    return HttpResponse("To order contact us at: item7goservice.gmail.com")
