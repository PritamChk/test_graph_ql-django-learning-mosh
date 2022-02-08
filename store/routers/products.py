from ninja import Router

from ..models import Product


product_router = Router(tags=["Product"])

@product_router.get("/",response=list[dict[str,str|float]])
def hello_prod(request,offset:int=0,limit:int=10):
    qs = Product.objects.all()
    return [{"title":p.title,"price": p.price } for p in qs[offset:offset+limit] ]