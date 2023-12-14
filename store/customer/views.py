from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Product
from .forms import CustomerProductForm

def customer_product_list(request):
    products = Product.objects.all()
    return render(request, 'customer/product_list.html', {'products': products})

def customer_product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'customer/product_detail.html', {'product': product})

def customer_purchase_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.purchased = True
        product.purchase_date = timezone.now()
        product.save()
        return redirect('customer_product_list')
    return render(request, 'customer/purchase_product.html', {'product': product})
