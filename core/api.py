from ninja import NinjaAPI
from store.routers.products import product_router


api = NinjaAPI()

api.add_router(prefix='/product',router=product_router)

@api.get("/hello")
def hello(request):
    return "Hello world"