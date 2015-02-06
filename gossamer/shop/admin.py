from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Product, Address, Order, Purchase
from .forms import CustomerAdmin

# Register your models here.
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Purchase)

try:
    admin.site.unregister(get_user_model())
finally:
    admin.site.register(get_user_model(), CustomerAdmin)
