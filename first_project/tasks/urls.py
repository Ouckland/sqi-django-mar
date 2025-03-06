from django.urls import path, include
from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("tasks/", views.all_tasks, name="tasks"),
]