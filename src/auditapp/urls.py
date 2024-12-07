from django.urls import path
from .views import ProductCreateView, ProductRetrieveUpdateView,LoginAPIView
from .views import login_view, logout_view, create_product, product_list
urlpatterns = [
    path('api/products/', ProductCreateView.as_view(), name='product-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateView.as_view(), name='product-retrieve-update'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
]
