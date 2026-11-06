import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
DB_NAME = os.getenv("POSTGRES_DB")

required_variables = {
    "POSTGRES_USER": DB_USER,
    "POSTGRES_PASSWORD": DB_PASSWORD,
    "POSTGRES_HOST": DB_HOST,
    "POSTGRES_DB": DB_NAME,
}

missing = [
    name for name, value in required_variables.items()
    if not value
]

if missing:
    raise RuntimeError(
        f"Missing database environment variables: {', '.join(missing)}"
    )

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)