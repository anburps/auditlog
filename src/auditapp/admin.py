from django.contrib import admin

from auditlog.registry import auditlog  
from auditapp.models import User
admin.site.register(User)

from auditapp.models import Product
admin.site.register(Product)
