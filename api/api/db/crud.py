#
# db interaction logic goes here.
#
from typing import List
from time import time
from pymongo.collection import Collection
from bson.objectid import ObjectId
from ..pydantic_models import (
    RecordID,
    RecordIn,
    RecordOut,
)


def get_all_records(
    records_collection: Collection,
):
    cursor = records_collection.find()
    records = []
    for r in cursor:
        if "_id" in r:
            r["_id"] = str(r["_id"])
        records.append(r)
    return records


def create_new_record(
    records_collection: Collection,
    record: RecordIn
):
    now = int(round(time() * 1000))
    record = record.dict()
    record.update(creationDate=now, lastModificationDate=now)
    bson_objectid = records_collection.insert_one(record).inserted_id
    result = {"_id": str(bson_objectid)}
    return result


def get_record_by_id(
    records_collection: Collection, record_id: str
):
    result = records_collection.find_one(ObjectId(record_id))
    result["_id"] = str(result["_id"])
    return result


def update_record(
    records_collection: Collection, record_id: str, record: dict
):
    record.update(lastModificationDate=int(round(time() * 1000)))
    if "_id" in record:
        del record["_id"]
    result = records_collection.find_one_and_update(
        {"_id": ObjectId(record_id)},
        { "$set": record },
        return_document=True,
    )
    result["_id"] = str(result["_id"])
    return result


def delete_record(
    records_collection: Collection, record_id: str
):
    result = records_collection.find_one_and_delete(
        # ObjectId(record_id),
        {"_id": ObjectId(record_id)},
    )
    result["_id"] = str(result["_id"])
    return result
