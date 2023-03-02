from django.urls import path
from . import views


urlpatterns = [
    path('', views.Menu, name='menu'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('update_item/', views.UpdateItem, name='update_item'),
    path('place_order/', views.PlaceOrder, name='place_order'),
]