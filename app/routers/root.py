"""Root router

Use for health checks, that's it.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """Use for health checks
    Returns {"message": "OK"}. That's it. Very basic health check
    """
    return {"message": "OK"}
