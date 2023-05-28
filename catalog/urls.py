from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, products, product_card

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('product_card', product_card, name='product_card'),
]

