from django.contrib import admin
from .models import Compte, CartLine, Order, OrderDetail

# Register your models here.
admin.site.register(Compte)
admin.site.register(CartLine)
admin.site.register(Order)
admin.site.register(OrderDetail)
