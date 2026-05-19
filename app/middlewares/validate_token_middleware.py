from fastapi import Request
from fastapi.responses import JSONResponse

from app.services.jwt_service import decode_token

API_KEY = "app-api-key-value"

EXCLUDED_PATHS = [
    "/v1/api/authentication/login",
    "/v1/api/authentication/register",
    "/health"
]

async def validate_token(request: Request, call_next):
    
    
    if request.method == "OPTIONS":
        return await call_next(request)

    # Exclude paths
    if request.url.path in EXCLUDED_PATHS:
        return await call_next(request)
    
    access_token = request.headers.get("access-token")
    print(f"accessToken: {access_token}")

    payload = decode_token(access_token)
    print(f"payload: {payload}")

    if not payload:
        return JSONResponse(
            status_code=401,
            content={
                "message": "No authorized"
            }
        )
    
    response = await call_next(request)

    return response
