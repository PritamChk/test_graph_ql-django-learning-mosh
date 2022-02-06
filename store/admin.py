from re import search
from django.contrib import admin
from django.contrib.admin import ModelAdmin 
from .models import *

admin.site.site_header ="Storefront Admin"
admin.site.index_title = "Admin"

@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ["title"]


# admin.site.register(Customer)
@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display =("first_name","last_name","membership","Age")
    list_editable = ["membership"]
    ordering = ("birth_date","first_name","last_name")
    list_per_page = 20
    search_fields = ["first_name__istartswith","last_name__istarts_with"]
    
    @admin.display(ordering='birth_date')
    def Age(self,customer):
        # from dateutil.relativedelta import relativedelta as diff 
        from datetime import date
        age = 0
        try:
            age = int(date.today().year - customer.birth_date.year)
        except:
            age = "NA"
        return age
        
            
    

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["title","price","inventory"]
    list_editable = ["price","inventory"]
    list_per_page = 20


admin.site.register(Cart)

admin.site.register(CartItems)

admin.site.register(Order)

admin.site.register(OrderItem)



# Register your models here.
