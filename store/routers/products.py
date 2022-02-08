from ninja import Router
from django.db.models import F,Q
from store.schema import ProductOut
from ..models import Product,Order,OrderItem


product_router = Router(tags=["Product"])

@product_router.get("/",response=list[ProductOut])
def hello_prod(request,offset:int=0,limit:int=10):
    qs = Product.objects.filter(promotions__isnull = False)
    
    return [ p for p in qs[offset:offset+limit] ]

@product_router.get("/ordered",response=list[ProductOut])
def get_ordered_prod(request,offset:int=0,limit:int=10):
    qs = Product.objects.filter(id__in = OrderItem.objects.values("product_id").distinct())
    return [ p for p in qs[offset:offset+limit] ]