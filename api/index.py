import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI(
    title="Retro GraphQL API",
    description="GraphQL API for retrospectives using FastAPI",
    version="0.1.0",
    docs_url='/api',
    openapi_url='/api/openapi.json',
    redoc_url=None
)
app.include_router(graphql_app, prefix="/graphql")
