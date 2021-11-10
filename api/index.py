from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"


# Create executable schema instance
schema = make_executable_schema(type_defs, query)

app = FastAPI(
    title="Retro GraphQL API",
    description="GraphQL API for retrospectives using FastAPI",
    version="0.1.0",
    docs_url='/api',
    openapi_url='/api/openapi.json',
    redoc_url=None
)
app.mount("/graphql", GraphQL(schema, debug=True))
