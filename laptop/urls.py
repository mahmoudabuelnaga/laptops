from django.urls import path, include
from django_filters.views import FilterView
from .models import Laptop
from .filter import LaptopFilter
from .views import prodact, product_detail


urlpatterns = [
    path('', prodact , name='filter_lap'),
    path('<int:pk>-<slug:slug>/', product_detail, name='product_detail'),
]
