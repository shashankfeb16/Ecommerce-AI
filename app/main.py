from fastapi import FastAPI

from app.api.v1.routes import router as api_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(
    api_router,
    prefix=settings.api_prefix,
)

@app.get("/")
async def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }