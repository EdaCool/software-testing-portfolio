import pytest


@pytest.mark.smoke
def test_get_booking_ids(booking_api):
    response = booking_api.get_booking_ids()

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.crud
def test_create_and_get_booking(booking_api, valid_booking_payload):
    # 创建 booking
    create_resp = booking_api.create_booking(valid_booking_payload)

    assert create_resp.status_code == 200
    body = create_resp.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == valid_booking_payload["firstname"]

    booking_id = body["bookingid"]

    # 查询刚创建的 booking
    get_resp = booking_api.get_booking(booking_id)

    assert get_resp.status_code == 200
    assert get_resp.json()["lastname"] == valid_booking_payload["lastname"]


@pytest.mark.crud
def test_update_booking(booking_api, valid_booking_payload, token):
    # 创建一条数据用于更新
    create_resp = booking_api.create_booking(valid_booking_payload)
    booking_id = create_resp.json()["bookingid"]

    updated_payload = valid_booking_payload.copy()
    updated_payload["firstname"] = "Tom"
    updated_payload["totalprice"] = 222

    update_resp = booking_api.update_booking(booking_id, updated_payload, token)

    assert update_resp.status_code == 200
    assert update_resp.json()["firstname"] == "Tom"
    assert update_resp.json()["totalprice"] == 222


@pytest.mark.crud
def test_delete_booking(booking_api, valid_booking_payload, token):
    create_resp = booking_api.create_booking(valid_booking_payload)
    booking_id = create_resp.json()["bookingid"]

    delete_resp = booking_api.delete_booking(booking_id, token)
    # 有些接口返回201也表示成功
    assert delete_resp.status_code in [200, 201]

    # 确认已删除
    get_resp = booking_api.get_booking(booking_id)
    assert get_resp.status_code == 404

