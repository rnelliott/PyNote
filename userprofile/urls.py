from django.conf.urls import url
from .views import update_profile

urlpatterns = [
    url(r'^update/$', update_profile, name='update_profile'),
    ]
