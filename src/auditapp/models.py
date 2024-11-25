
from django.db import models
from auditlog.registry import auditlog
from django.contrib.auth.models import User as abstractUser

class User(abstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
auditlog.register(User)

class Product(models.Model):
    user = model.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
auditlog.register(Product)
