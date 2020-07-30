"""ep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from .views import create_form, url_hash, url_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shortener/', create_form, name='shortener'),
    url(r'^link/(?P<url>[0-9A-Za-z_\-@.]+)/(?P<hash>[0-9A-Za-z_\-@.]+)/', url_hash, name='shortened'),
    url(r'^link/(?P<url>[0-9A-Za-z_\-@.]+)/', url_path, name='url'),
]
