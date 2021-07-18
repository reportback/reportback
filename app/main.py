"""Entry Point for Report Back

This is a draft for understanding how the API might go.
"""
from fastapi import FastAPI

from app.routers import contacts, root

app = FastAPI()
app.include_router(root.router)
app.include_router(contacts.router)
