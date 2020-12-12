from fastapi import FastAPI

def get_api() -> FastAPI:
    api = FastAPI()
    return api

api = get_api()
