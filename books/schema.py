from dataclasses import fields
import graphene as gfin
from graphene_django import DjangoObjectType as DOT
from .models import Books

class BooksType(DOT):
    class Meta:
        model = Books
        fields = ("id","title","description")
        
class Query(gfin.ObjectType):
    all_books = gfin.List(BooksType)
    
    def resolve_all_books(root,info):
        return Books.objects.all()
    
schema = gfin.Schema(query=Query)