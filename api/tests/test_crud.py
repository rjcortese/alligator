# import pytest
# from datetime import datetime
# from alligator_api.db.crud import (
#     get_all_records,
#     create_new_record,
#     get_record_by_id,
#     update_record,
#     delete_record,
# )


# pytestmark = pytest.mark.asyncio

# rA = {
#     "timestamp": 1608005533467,
#     "value1": "salty",
#     "value2": 2.3,
#     "value3": True,
# }

# rB = {
#     "timestamp": 1603005511467,
#     "value1": "scaley",
#     "value2": 123123.123123,
#     "value3": False,
# }



# async def test_get_all_records_empty(mongodb_collection):
#     records = await get_all_records(mongodb_collection)
#     assert records == []


# async def test_create_new_record(mongodb_collection):
#     record = await create_new_record(mongodb_collection, rA)
#     assert rA == record


# async def test_get_record_by_id(mongodb_collection):
#     record = await get_record_by_id(mongodb_collection, rid)


# async def test_update_record(mongodb_collection):
#     record = await update_record(mongodb_collection)


# async def test_delete_record(mongodb_collection):
#     record = await delete_record(mongodb_collection)


# async def test_get_all_records(mongodb_collection):
#     records = await get_all_records(mongodb_collection)

