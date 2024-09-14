from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
#not work deloet
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index,name="index"),
    
]
