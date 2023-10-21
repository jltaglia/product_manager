# product_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('modify_products/', views.modify_products, name='modify_products'),
]