from django.contrib import admin

from school.models import *

# Register your models here.

admin.site.register(Product)

admin.site.register(OrderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'transaction_id']
