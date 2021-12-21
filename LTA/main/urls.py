from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
    path('about/', views.about),
    path('cart/', views.cart)
]