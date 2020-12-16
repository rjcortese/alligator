from fastapi import FastAPI
from .routes import records

api = FastAPI(
    title="Alligator",
    description="So scaley. So salty.",
)
api.include_router(records)
