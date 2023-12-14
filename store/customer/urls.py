from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.customer_product_list, name='customer_product_list'),
    path('product_detail/<int:pk>/', views.customer_product_detail, name='customer_product_detail'),
    path('purchase_product/<int:pk>/', views.customer_purchase_product, name='customer_purchase_product')
]