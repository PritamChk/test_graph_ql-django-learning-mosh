from ninja import Router

from store.schema import ProductOut

from ..models import Product


product_router = Router(tags=["Product"])

@product_router.get("/",response=list[ProductOut])
def hello_prod(request,offset:int=0,limit:int=10):
    qs = Product.objects.filter(promotions__isnull = False)
    
    return [ p for p in qs[offset:offset+limit] ]