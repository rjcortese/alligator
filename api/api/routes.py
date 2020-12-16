from typing import List, Optional, Dict
from pymongo.collection import Collection
from fastapi import (
    APIRouter,
    Depends,
)
from . import db
from .pydantic_models import (
    RecordID,
    RecordIn,
    RecordOut,
)


records = APIRouter(prefix="/api")


@records.get("/list", response_model=List[Optional[RecordOut]])
def list_records(
    collection: Collection = Depends(db.get_records_collection),
):
    return db.get_all_records(collection)


@records.post("/create", response_model=RecordID)
def create_record(
    record: RecordIn,
    collection: Collection = Depends(db.get_records_collection),
):
    created_id = db.create_new_record(collection, record)
    return created_id


@records.get("/read/{record_id}", response_model=RecordOut)
def read_record(
    record_id: str,
    collection: Collection = Depends(db.get_records_collection),
):
    record = db.get_record_by_id(collection, record_id)
    return record


@records.patch("/modify/{record_id}", response_model=RecordOut)
def modify_record(
    record_id: str,
    record: Dict,
    collection: Collection = Depends(db.get_records_collection),
):
    record = db.update_record(collection, record_id, record)
    return record


@records.delete("/remove/{record_id}", response_model=RecordOut)
def delete_record(
    record_id: str,
    collection: Collection = Depends(db.get_records_collection),
):
    return db.delete_record(collection, record_id)
