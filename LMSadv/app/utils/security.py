from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY ,ALGORITHM
SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(hours=2)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    print("TOKEN RECEIVED:", token)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD:", payload)

        user_id = payload.get("user_id")
        role = payload.get("role")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"user_id":user_id,"role":role}

    except JWTError as e:
        print("JWT ERROR:", str(e))
        raise HTTPException(status_code=401, detail="Invalid token")