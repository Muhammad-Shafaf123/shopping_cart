from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(ProductMen)
admin.site.register(ProductWomen)
admin.site.register(ProductKids)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)



