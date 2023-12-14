from django.urls import path
from . import views

urlpatterns = [
    path('start_page/', views.product_list, name='product_list'),
    path('edit_product/<int:pk>/', views.product_edit, name='product_edit'),
    path('delete_product/<int:pk>/', views.product_delete, name='product_delete'),
    path('add_product/', views.product_add, name='product_add')
]