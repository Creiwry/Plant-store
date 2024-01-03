from django.shortcuts import render
from .models import Product

# Create your views here.

def product_detail_view(request, product_id, *args, **kwargs):
    product = Product.objects.get(id=product_id)
    my_context = {
            "product": product,
            }
    return render(request, "product/detail.html", my_context)
