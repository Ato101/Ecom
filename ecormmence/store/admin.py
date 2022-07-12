from django.contrib import admin

from .models import Order,Product,Customer,ShippingAddress,OrderItem

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
