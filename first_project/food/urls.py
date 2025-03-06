from django.urls import path, include
from . import views

urlpatterns = [
    path("our-menu/", views.menu, name="our-menu"),
    path("contact-us/", views.contact, name="contact-us")
]
