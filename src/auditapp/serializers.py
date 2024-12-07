from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email','password']
        extra_kwargs = {
            'password': {'write_only': True}  
        }
        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [ 'user', 'name', 'price']

        def create(self, validated_data):
            user = self.context['request'].user  
            return Product.objects.create(user=user, **validated_data)




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("User account is inactive.")

        data['user'] = user
        return data