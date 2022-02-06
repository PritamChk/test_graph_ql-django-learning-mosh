from django.urls import path,include
from graphene_django.views import GraphQLView as gql_view
from books.schema import schema

urlpatterns = [
        path("graphql",gql_view.as_view(graphiql=True,schema=schema))
    ]