from django.shortcuts import render
from .models import Product
from projects.models import Projects, Category


# Create your views here.
def all_products(request):
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    products = Product.objects.all()
    return render(request, "products.html", {"products": products,
                                             "projects": projects,
                                             "categories": categories})
