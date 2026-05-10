from fastapi import FastAPI
from app.routes.authentication_routes import router as authentication_routes
from app.routes.financial_routes import router as financial_routes

from app.middlewares.validate_token_middleware import validate_token

app = FastAPI()

# Registrar middleware
app.middleware("http")(validate_token)

app.include_router(authentication_routes)
app.include_router(financial_routes)

