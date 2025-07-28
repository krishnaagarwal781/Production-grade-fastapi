from fastapi import FastAPI
from app.routers import purpose
from app.config import settings

app = FastAPI(debug=settings.DEBUG)
app.include_router(purpose.router)
