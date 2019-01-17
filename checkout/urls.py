from django.conf.urls import url
from .views import checkout

urlpattern = [
    url(r'^$', checkout, name="checkout"),
]