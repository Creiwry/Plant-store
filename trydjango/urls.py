"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from pages.views import home_view, contact_view, about_view, signup_view, signin_view
from products.views import product_detail_view, product_delete_view, product_create_view, product_update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view),
    path('signin/', LoginView.as_view(template_name='users/signin.html'), name='login'),
    path('', home_view, name='home'),
    path('product/<int:product_id>', product_detail_view, name="product_detail"),
    path('product/<int:product_id>/update', product_update_view, name="product_update"),
    path('product/<int:product_id>/delete', product_delete_view, name="product_delete"),
    path('product/create', product_create_view, name="product_create"),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path("__reload__/", include("django_browser_reload.urls"))
]
