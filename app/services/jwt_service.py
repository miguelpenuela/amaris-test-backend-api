from datetime import timedelta, datetime, timezone

from pydantic import BaseModel

import jwt

SECRET_KEY = "bb60da37e931f59eb5ead593270c88bb6524256b80198bd9d484faf6e151a09c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10


class Token(BaseModel):
    access_token: str
    token_type: str

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=10)

    payload.update({
        "exp": expire
    })

    return jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception:
        return None