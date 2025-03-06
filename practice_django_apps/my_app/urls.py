from django.urls import path
from my_app import views

app_name = "my_app"
urlpatterns = [
    path("my_app/", views.welcome, name="my_app"),
]