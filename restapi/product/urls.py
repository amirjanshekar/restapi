from .views import product_list
from django.urls import path

urlpatterns = [
    path('product/', product_list),
]
