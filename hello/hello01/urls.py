from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test1/',views.test),
    # http://127.0.0.1/hello01/test1
    
]
