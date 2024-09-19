from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    top_customers = Order.top_5_customers()
    return render(request, 'index.html', {'top_customers': top_customers})
