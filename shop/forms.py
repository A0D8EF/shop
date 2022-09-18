from django import forms

from .models import Product

class CategorySearchForm(forms.ModelForm):

    class Meta:
        model   = Product
        fields  = ["category"]
    
class ProductMaxPriceForm(forms.Form):
    max_price   = forms.IntegerField()

class ProductMinPriceForm(forms.Form):
    min_price   = forms.IntegerField()