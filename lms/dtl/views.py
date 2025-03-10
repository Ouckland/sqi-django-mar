from django.shortcuts import render

# Create your views here.
def tasks(requests):
    context = {
        "user": "Korede",
        "cart_items": ["tomato", "strawberry", "vanilla ice cream", "burger", "cake"],
        "is_favorite": True,
        "no_of_items_in_cart": 5
    }
    return render(requests, "dtl/tasks.html", context)
