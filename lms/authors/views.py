from django.shortcuts import render

# Create your views here.
def author_page(request):
    return render(request, "authors/authors-page.html")

def book_list(request):
    return render(request, "authors/book-list.html")