from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = "items"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["endpoint"] = "product"
        return context

class ProductCreateView(CreateView):
    # form_class = #TODO: ADD FORM TO VIEW
    model = Product
    fields = ["name", "price"]
    context_object_name = "item"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["endpoint"] = "product"
        return context


class ProductUpdateView(UpdateView):
    #TODO: ADD FORM TO VIEW
    model = Product
    fields = ["name", "price"]
    context_object_name = "item"
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["endpoint"] = "product"
        return context
    

class ProductDetailView(DetailView):
    model = Product
    fields = ["name", "price"]
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["endpoint"] = "product"
        return context
# from django.views import View