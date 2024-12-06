from rest_framework import generics, status
from rest_framework.response import Response  
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from .serializers import ProductSerializer
from .models import Product

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  

class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            set_actor(request.user)
            
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

from django.shortcuts import render, redirect
from .forms import ProductForm
@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user 
            product.save()
            return redirect('create_product')  
    else:
        form = ProductForm()
    
    return render(request, 'home.html', {'form': form})

def login