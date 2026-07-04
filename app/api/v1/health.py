from fastapi import APIRouter
from app.core.logging import logger
logger.info("Health endpoint called")
router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "healthy",
    }