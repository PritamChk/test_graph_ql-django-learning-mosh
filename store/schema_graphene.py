import graphene as gfn
from graphene_django import DjangoObjectType as DOT




class Query(gfn.ObjectType):
    hello = gfn.String(default_value="Hi!")

schema = gfn.Schema(query=Query)