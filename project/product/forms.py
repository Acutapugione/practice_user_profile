from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreationForm, ProductUpdateForm

def create_product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list_url')
    else:
        form = ProductCreationForm()
    return render(request, 'create_product.html', {'form': form})

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list_url')
    else:
        form = ProductUpdateForm(instance=product)
    return render(request, 'update_product.html', {'form': form})