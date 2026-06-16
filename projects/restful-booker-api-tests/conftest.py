import pytest
import yaml

from api.client import ApiClient
from api.booking_api import BookingApi


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def api_client(config):
    return ApiClient(config["base_url"], config["timeout"])


@pytest.fixture(scope="session")
def booking_api(api_client):
    return BookingApi(api_client)


@pytest.fixture(scope="session")
def token(config, booking_api):
    response = booking_api.create_token(config["username"], config["password"])
    assert response.status_code == 200
    assert "token" in response.json()
    return response.json()["token"]


@pytest.fixture
def valid_booking_payload():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-06-01",
            "checkout": "2026-06-10"
        },
        "additionalneeds": "Breakfast"
    }

