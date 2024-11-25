from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from auditlog.registry import auditlog
from auditlog.models import HistoryField

# Ensure Role is imported if it's defined elsewhere
# from .models import Role  # Uncomment if Role is in the same app

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='auditapp_user_set', 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='auditapp_user_permissions_set',  
        blank=True,
    )

    USERNAME_FIELD = "email"  
    REQUIRED_FIELDS = ["username"]  

    def __str__(self):
        return self.username

auditlog.register(User)

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.token


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoryField()


    def __str__(self):
        return self.name
auditlog.register(Product)
