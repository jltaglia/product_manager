# Create your views here.
# product_app/views.py
from django.shortcuts import render, redirect
from .models import Product
from .forms import FilterForm

def modify_products(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            price_percentage = form.cleaned_data['price_percentage']
            # Filter products based on user input
            products = Product.objects.filter(Price__gt=0)  # Modify this filter as needed

            # Apply percentage change to Price and Cost fields
            for product in products:
                product.Price += product.Price * (price_percentage / 100)
                product.Cost += product.Cost * (price_percentage / 100)
                product.save()

            return redirect('success_page')  # Create a success page in your app
    else:
        form = FilterForm()

    return render(request, 'product_app/modify_products.html', {'form': form})
