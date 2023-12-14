from django import forms
from .models import Product

class CustomerProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']