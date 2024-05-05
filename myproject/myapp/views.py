from django.shortcuts import render
from .models import User, Order
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def index(request):
    return render(request, 'home.html')

def orders(request):
    return render(request, 'orders.html')

def user_orders(request, name_id):
    name = User.objects.get(pk=name_id)
    orders = Order.objects.filter(name=name)
    return render(request, 'myapp/orders.html', {'name': name, 'orders': orders})

def user_orders_filtered(request, name_id):
    name = User.objects.get(pk=name_id)
    today = timezone.now()
    orders_last_week = Order.objects.filter(name=name, data__gte=today - timedelta(days=7))
    orders_last_month = Order.objects.filter(name=name, data__gte=today - timedelta(days=30))
    orders_last_year = Order.objects.filter(name=name, data__gte=today - timedelta(days=365))

    context = {
        'name': name,
        'orders_last_week': orders_last_week,
        'orders_last_month': orders_last_month,
        'orders_last_year': orders_last_year
    }
    return render(request, 'myapp/orders_filtered.html', context)