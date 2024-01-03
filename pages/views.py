from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    products = Product.objects.all()
    my_context = {
            "products": products,
            }
    return render(request, "home.html", my_context)

def about_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
