import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ENV = os.getenv("ENV", "development")

if ENV == "production":
    load_dotenv(".env.production")
elif ENV == "testing":
    load_dotenv(".env.testing")
else:
    load_dotenv(".env.development")


class Settings(BaseSettings):
    MONGO_URI: str
    DEBUG: bool = False
    ENV: str = ENV

settings = Settings()
