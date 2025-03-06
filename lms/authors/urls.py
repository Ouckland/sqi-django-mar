from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.author_page, name='author-page'),
    path('book-list/', views.book_list, name='book_list'),
]