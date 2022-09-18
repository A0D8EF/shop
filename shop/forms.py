from django import forms

from django.utils import timezone
from django.core.validators import MinValueValidator

from .models import Product

class CategorySearchForm(forms.ModelForm):

    class Meta:
        model   = Product
        fields  = ["category"]
    

class ProductMaxPriceForm(forms.Form):
    max_price   = forms.IntegerField()


class ProductMinPriceForm(forms.Form):
    min_price   = forms.IntegerField()


class StartReleaseForm(forms.Form):
    start_release = forms.DateField()


class EndReleaseForm(forms.Form):
    end_release = forms.DateField()

