from django import forms
from customer.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'purchase_date']

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']