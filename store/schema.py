from ninja.orm import create_schema
from store.models import Product,Promotion

PromotionOut = create_schema(Promotion)
ProductOut = create_schema(Product,fields=["title","price","description","promotions"],depth=1)
