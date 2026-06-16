import pytest


@pytest.mark.smoke
def test_create_token_success(booking_api, config):
    response = booking_api.create_token(config["username"], config["password"])

    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.negative
def test_create_token_with_wrong_password(booking_api, config):
    response = booking_api.create_token(config["username"], "wrong-password")

    assert response.status_code == 200
    assert response.json().get("reason") == "Bad credentials"

