# serializers.py
from rest_framework import serializers
from .models import Product, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email','password']

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Product
        fields = [ 'user', 'name', 'price']
