from django.urls import path
from .views import ProductCreateView, ProductRetrieveUpdateView,create_product

urlpatterns = [
    path('api/products/', ProductCreateView.as_view(), name='product-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateView.as_view(), name='product-retrieve-update'),
    path('products/create/', create_product, name='create_product'),
]
