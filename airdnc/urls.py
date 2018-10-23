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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts import urls as urls_accounts
from accounts.views import index

urlpatterns = [
    # if user goes to admin/, load admin app
    url(r'^admin/', admin.site.urls),
    # if user goes to root/index, redirect to projects/
    url(r'^$', RedirectView.as_view(url='projects/'), name='index'),
    # if user goes to projects/, parse url in urls.py in projects app
    url(r'projects/', include('projects.urls')),
    # if user goes to media/, use RegEx to point to a path of a file
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # if user goes to accounts/, parse url in urls.py i accounts app
    url(r'^accounts/', include(urls_accounts)),
]
