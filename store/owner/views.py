from django.shortcuts import render, redirect, get_object_or_404
from customer.models import Product
from .forms import ProductForm, ProductAddForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'owner/product_list.html', {'products': products})
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'owner/product_edit.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'owner/product_delete.html', {'product': product})
def product_add(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductAddForm()
    return render(request, 'owner/product_add.html', {'form': form})
