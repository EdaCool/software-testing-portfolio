class BookingApi:
    def __init__(self, client):
        self.client = client

    def create_token(self, username, password):
        return self.client.post(
            "/auth",
            json={"username": username, "password": password},
            headers={"Content-Type": "application/json"},
        )

    def get_booking_ids(self, params=None):
        return self.client.get("/booking", params=params)

    def get_booking(self, booking_id):
        return self.client.get(f"/booking/{booking_id}", headers={"Accept": "application/json"})

    def create_booking(self, payload):
        return self.client.post(
            "/booking",
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )

    def update_booking(self, booking_id, payload, token):
        return self.client.put(
            f"/booking/{booking_id}",
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f"token={token}",
            },
        )

    def delete_booking(self, booking_id, token):
        return self.client.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
        )

