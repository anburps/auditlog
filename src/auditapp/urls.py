from django.urls import path
from .views import ProductCreateView, ProductRetrieveUpdateView

urlpatterns = [
    path('api/products/', ProductCreateView.as_view(), name='product-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateView.as_view(), name='product-retrieve-update'),
]
