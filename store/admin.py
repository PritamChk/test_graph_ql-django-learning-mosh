from django.contrib import admin
from .models import *

admin.site.site_header ="Storefront Admin"
admin.site.index_title = "Admin"

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Promotion)



# Register your models here.
