
from django.urls import path

from .views import (
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    OrderSummaryView
     )
app_name = 'order'

urlpatterns = [
    path('add-to-cart/<uuid:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<uuid:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<pk>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('order-summary/',OrderSummaryView.as_view(), name='order-summary')
]
