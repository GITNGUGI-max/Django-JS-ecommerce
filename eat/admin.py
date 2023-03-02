from django.contrib import admin

from eat.models import *


class CustomerAdmin(admin.ModelAdmin):

    pass

admin.site.register(Customer, CustomerAdmin)

@admin.register(MenuItems)

class MenuItemsAdmin(admin.ModelAdmin):

    pass

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
