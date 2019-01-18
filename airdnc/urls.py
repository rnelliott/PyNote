"""airdnc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve

from accounts import urls as urls_accounts
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from products import urls as urls_products
from userprofile import urls as urls_userprofile
from products.views import all_products
from projects.views import index

from .settings import MEDIA_ROOT

urlpatterns = [
    # if user goes to admin/, load admin app
    url(r'^admin/', admin.site.urls),
    # if user goes to root/index, redirect to projects/
    url(r'^$', index, name='index'),
    # if user goes to accounts/, parse url in urls.py i accounts app
    url(r'^accounts/', include(urls_accounts)),
    # if user goes to projects/, parse url in urls.py in projects app
    url(r'projects/', include('projects.urls')),
    # Tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    # Products
    url(r'^products/', include(urls_products, namespace="products")),
    # Social auth URLS
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # Cart
    url(r'^cart/', include(urls_cart)),
    # Checkout
    url(r'^checkout/', include(urls_checkout)),
    # Profile
    url(r'^profile/', include(urls_userprofile)),
    # if user goes to media/, use RegEx to point to a path of a file
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
