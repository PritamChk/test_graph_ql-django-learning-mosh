
import graphene as gfn
from graphene_django import DjangoObjectType as DOT
from store.models import *


class CustomerType(DOT):
    class Meta:
        model =Customer
        fields = ("first_name","email","membership")


class ProductType(DOT):
    class Meta:
        model = Product
        fields = ("title","price","promotions","collection")

class PromotionType(DOT):
    class Meta:
        model = Promotion
        fields = ("discount","description")   
             
class CollectionType(DOT):
    class Meta:
        model = Collection
        fields = ("id","title")        

class OrderType(DOT):
    class Meta:
        model = Order
        fields = ("payment_status","customer")
        
class OrderItemType(DOT):
    class Meta:
        model = OrderItem
        fields = ("order","product","quantity","unit_cost")


class Query(gfn.ObjectType):
    get_products = gfn.List(ProductType)
    get_promo = gfn.List(PromotionType)
    get_collection = gfn.List(CollectionType)
    get_customer = gfn.List(CustomerType)
    get_customer_bought_products = gfn.List(CustomerType)
    # def resolve_get_collection(root,info):
    #     return Collection.objects.all()
    # 
    
    # def resolve_get_customer_bought_products(root,info):
    #     return OrderItem.objects.all().filter()
    
    def resolve_get_customer(root,info):
        return Customer.objects.all()
    
    def resolve_get_promo(root,info):
        return Promotion.objects.all()
    
    def resolve_get_products(root,info):
        return Product.objects.all().order_by("id")
    
    # def resolve_products_with_promotion(root,info):
    #     qs = Product.objects.filter(promotions__isnull=False)
    #     return qs

schema = gfn.Schema(query=Query)