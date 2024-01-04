from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_detail_view(request, product_id, *args, **kwargs):
    product = get_object_or_404(Product, id=product_id)
    my_context = {
            "product": product,
            }
    return render(request, "products/product_detail.html", my_context)

def product_create_view(request):
    initial_data = {
            'title': "My plant title",
            }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        print(form.errors)

    context= {
            'form': form
            }

    return render(request, "products/product_create.html", context)


def product_update_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    context= {
            'form': form,
            'product_id': product.id,
            }

    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        print(form.errors)

    return render(request, "products/product_update.html", context)

def product_delete_view(product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('/')
