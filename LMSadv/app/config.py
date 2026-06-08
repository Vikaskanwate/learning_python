import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URL = os.getenv("MONGO_URL")
ALGORITHM = os.getenv("ALGORITHM")