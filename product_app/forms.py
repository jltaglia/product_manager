# product_app/forms.py
from django import forms

class FilterForm(forms.Form):
    price_percentage = forms.FloatField(label="Price Percentage")
    # Add other fields for filtering here
