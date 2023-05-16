from django.contrib import admin

from school.models import *

# Register your models here.

admin.site.register(Product)

admin.site.register(OrderItem)

# class OrderPositionInline(admin.TabularInline):
#     model = OrderItem
#     extra = 2

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'transaction_id']