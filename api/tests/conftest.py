import pytest
from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure


@pytest.fixture(scope="session")
def mongo_service(docker_ip, docker_services) -> str:
    """
    Spin up mongodb server for testing.
    Return a url to the service.
    """
    port = docker_services.port_for("db", 27017)
    url = f"mongodb://tester:testing@{docker_ip}:{port}"

    def is_responsive(url):
        try:
            client = MongoClient(url)
            result = client.admin.command("ping")
            return True
        except ConnectionFailure:
            return False

    docker_services.wait_until_responsive(
        timeout=15.0, pause=0.2, check=lambda: is_responsive(url)
    )

    return url


@pytest.fixture
def alligator_records(mongo_service) -> Collection:
    return MongoClient(mongo_service).alligator.records


@pytest.fixture
def json_A():
    return {
        "timestamp": 1608034045752,
        "value1": "hehe",
        "value2": 345.123,
        "value3": True,
    }


@pytest.fixture
def json_B():
    return {
        "timestamp": 1607084045752,
        "value1": "Crieky!",
        "value2": 102923293.12313,
        "value3": False,
    }
