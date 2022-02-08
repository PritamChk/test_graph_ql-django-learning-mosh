
import graphene as gfn
from graphene_django import DjangoObjectType as DOT
from store.models import *

class ProductType(DOT):
    class Meta:
        model = Product
        fields = ("id","title","price","description","inventory","last_update")

class PromotionType(DOT):
    class Meta:
        model = Promotion
        fields = ("discount","description")        

class ProductWithPromotionType(DOT):
    class Meta:
        model = Product
        exclude = ("collection",)

class Query(gfn.ObjectType):
    get_products = gfn.List(ProductType)
    products_with_promotion = gfn.List(ProductWithPromotionType)
    get_promo = gfn.List(PromotionType)
    
    def resolve_get_promo(root,info):
        return Promotion.objects.all()
    
    def resolve_get_products(root,info):
        return Product.objects.all().order_by("id")
    
    def resolve_products_with_promotion(root,info):
        qs = Product.objects.filter(promotions__isnull=False)
        return qs

schema = gfn.Schema(query=Query)