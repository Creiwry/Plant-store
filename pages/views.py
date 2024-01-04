from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signin.html', {'form': form})
