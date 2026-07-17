import os


DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)