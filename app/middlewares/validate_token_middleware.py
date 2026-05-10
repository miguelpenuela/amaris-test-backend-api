from fastapi import Request
from fastapi.responses import JSONResponse

API_KEY = "app-api-key-value"

EXCLUDED_PATHS = [
    "/v1/api/authentication/login",
    "/v1/api/authentication/register"
]

async def validate_token(request: Request, call_next):

    # Exclude paths
    if request.url.path in EXCLUDED_PATHS:
        return await call_next(request)
    
    api_key = request.headers.get("x-api-key")

    if api_key != API_KEY:
        return JSONResponse(
            status_code=401,
            content={
                "message": "No authorized"
            }
        )
    
    response = await call_next(request)

    return response
