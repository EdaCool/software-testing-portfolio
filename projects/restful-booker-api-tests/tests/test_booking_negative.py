import pytest


@pytest.mark.negative
def test_get_not_existing_booking(booking_api):
    response = booking_api.get_booking(999999999)

    assert response.status_code == 404


@pytest.mark.negative
def test_update_booking_without_token(booking_api, valid_booking_payload):
    create_resp = booking_api.create_booking(valid_booking_payload)
    booking_id = create_resp.json()["bookingid"]

    updated_payload = valid_booking_payload.copy()
    updated_payload["firstname"] = "NoToken"

    response = booking_api.update_booking(booking_id, updated_payload, token="")

    assert response.status_code in [403, 401]

