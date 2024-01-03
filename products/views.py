from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_detail_view(request, product_id, *args, **kwargs):
    product = Product.objects.get(id=product_id)
    my_context = {
            "product": product,
            }
    return render(request, "products/product_detail.html", my_context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    context= {
            'form': form
            }

    return render(request, "products/product_create.html", context)
