from django.contrib import admin

# Register your models here.

from . models import Category, BestServedAt, Menu, Order, OrderItem, TableInfo, Customer



admin.site.register(Customer)

admin.site.register(Category)
admin.site.register(BestServedAt)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TableInfo)
