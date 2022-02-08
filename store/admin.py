from django.contrib import admin
from django.contrib.admin import ModelAdmin,TabularInline
from .models import *

admin.site.site_header = "Storefront Admin"
admin.site.index_title = "Admin"


@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    empty_value_display = '-empty-'



@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    empty_value_display: str = 'NA'
    # list_display_links =("full_name",)
    list_display = ("full_name", "membership", "Age")  # ,"birth_date")
    list_editable = ["membership"]
    ordering = ("birth_date", "first_name", "last_name")
    list_per_page = 20
    search_fields = ["first_name__istartswith",
                     "last_name__istartswith", "phone"]

    @admin.display(ordering=("first_name", "last_name"))
    def full_name(self, cust: Customer):
        return f'{cust.first_name} {cust.last_name}'

    @admin.display(ordering='birth_date')
    def Age(self, customer):
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
    empty_value_display = '-empty-'
    list_display = ["title", "price", "inventory"]
    list_editable = ["price", "inventory"]
    list_per_page = 20
    search_fields = ["title"]
    autocomplete_fields = ["collection"]



class CartItemsInline(TabularInline):
    autocomplete_fields = ["product",]
    min_num = 0
    extra =1
    max_num = 10
    model = CartItems
    

@admin.register(CartItems)
class CartItemsAdmin(ModelAdmin):
    list_display = ["cart_id","product","quantity"]
    list_editable = ["quantity"]




@admin.register(Cart)
class CartAdmin(ModelAdmin):
    inlines = [CartItemsInline]

class OrderItemsInline(TabularInline):
    autocomplete_fields = ["product",]
    min_num = 0
    extra =1
    max_num = 10
    model = OrderItem

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    autocomplete_fields = ("customer",)
    inlines = [OrderItemsInline]
    list_display = ("id", "payment_status", "customer")
    list_editable = ("payment_status",)
    search_fields = ["payment_status"]


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    # list_display_links = ("customer_name",)
    list_display = ("order_id","customer_name","quantity","unit_cost","original_mrp")
    list_editable = ("unit_cost","quantity")
    
    @admin.display(ordering="quantity")
    def customer_name(self,orderitem:OrderItem):
        return orderitem.order.customer.first_name
    
    @admin.display()
    def original_mrp(self,orderitem:OrderItem):
        return orderitem.product.price

@admin.register(Promotion)
class PromotionAdmin(ModelAdmin):
    list_display = ["id","description","discount"]
    list_editable = ["discount",]
    ordering = ["-discount"]