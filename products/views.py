from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Product


# Create your views here.
@login_required
def all_products(request):
    products = Product.objects.all()

    return render(request, "products.html", {"products": products})
