from django.contrib import admin
from .models import orderItem,OrderModel

# Register your models here.
admin.site.register(OrderModel)
admin.site.register(orderItem)
