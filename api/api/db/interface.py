#
# Any code for db connections goes here.
#
from pymongo.mongo_client import MongoClient
from ..config import get_settings

settings = get_settings()
client = MongoClient(
    host=settings.db_host,
    port=settings.db_port,
    username=settings.db_username,
    password=settings.db_password.get_secret_value(),
)


def get_client():
    return client


def get_alligator_db():
    client = get_client()
    return client.alligator


def get_records_collection():
    db = get_alligator_db()
    return db.records
