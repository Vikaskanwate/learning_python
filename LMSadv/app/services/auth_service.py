from app.database import users_collection
from app.utils.security import hash_password, verify_password, create_token

def register_user(user):
    existing = users_collection.find_one({"email": user.email})
    if existing:
        raise Exception("User already exists")

    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["role"] = "user" 

    users_collection.insert_one(user_dict)
    return {"message": "User registered"}

def login_user(user):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user:
        raise Exception("Invalid credentials")

    if not verify_password(user.password, db_user["password"]):
        raise Exception("Invalid credentials")

    token = create_token({
        "user_id": str(db_user["_id"]),
        "role":db_user.get("role","user")
        })
    return {
    "access_token": token,
    "token_type": "bearer"
}