import pytest
from fastapi.testclient import TestClient
from bson.objectid import ObjectId
from api.main import api


client = TestClient(api)


def test_api_list_empty(mongo_service):
    response = client.get("/api/list")
    assert response.status_code == 200
    assert response.json() == []


def test_api_create_one(mongo_service, json_A):
    response = client.post("/api/create", json=json_A)
    assert response.status_code == 200
    res_json = response.json()
    oidA = res_json["_id"]
    assert ObjectId.is_valid(oidA)
    # store this for later
    pytest.oidA = oidA


def test_api_read_one(mongo_service, json_A):
    json_A_with_id = dict(json_A, _id=pytest.oidA)
    response = client.get(f"/api/read/{pytest.oidA}")
    assert response.status_code == 200
    assert response.json() == json_A_with_id


def test_api_list_one(mongo_service, json_A):
    json_A_with_id = dict(json_A, _id=pytest.oidA)
    response = client.get("/api/list")
    assert response.status_code == 200
    assert response.json() == [json_A_with_id]


def test_api_create_one_more(mongo_service, json_B):
    response = client.post("/api/create", json=json_B)
    assert response.status_code == 200
    oidB = response.json()["_id"]
    assert ObjectId.is_valid(oidB)
    # store this for later
    pytest.oidB = oidB


def test_api_modify_one(mongo_service, json_A):
    json_A_with_id = dict(json_A, _id=pytest.oidA)
    new_fields = {
        "value1": "hohoho",
        "value2": 9999.99,
    }
    response = client.patch(f"/api/modify/{pytest.oidA}", json=new_fields)
    assert response.status_code == 200
    after_update = dict(json_A_with_id, **new_fields)
    assert response.json() == after_update


def test_api_list_two(mongo_service, json_A, json_B):
    json_A_with_id = dict(json_A, _id=pytest.oidA)
    new_fields = {
        "value1": "hohoho",
        "value2": 9999.99,
    }
    after_update = dict(json_A_with_id, **new_fields)
    json_B_with_id = dict(json_B, _id=pytest.oidB)

    response = client.get("/api/list")
    assert response.status_code == 200
    assert response.json() == [after_update, json_B_with_id]


def test_api_delete_one(mongo_service, json_B):
    json_B_with_id = dict(json_B, _id=pytest.oidB)
    response = client.delete(f"/api/remove/{pytest.oidB}")
    assert response.status_code == 200
    assert response.json() == json_B_with_id
