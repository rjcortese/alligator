from fastapi import FastAPI
from .routes import records

api = FastAPI()
api.include_router(records)
