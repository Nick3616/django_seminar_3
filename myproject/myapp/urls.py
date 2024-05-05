from django.urls import path
from . import views
from .views import user_orders

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:name_id>/', views.user_orders, name='user_orders'),
    path('orders_filtered/<int:name_id>/', views.user_orders_filtered, name='user_orders_filtered'),
]
