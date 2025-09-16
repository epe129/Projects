from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
]

