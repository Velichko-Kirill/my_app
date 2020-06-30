from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    url(r'', views.login),
    path('', include('social_django.urls'))
]