import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# 预置数据
next_id = 100
bookings = {}

# ---------- Auth ----------
@app.route('/auth', methods=['POST'])
def create_token():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "password123":
        return jsonify({"token": "mock-token-abc123"})
    else:
        return jsonify({"reason": "Bad credentials"}), 200  # 注意原 API 返回 200

# ---------- Booking ----------
@app.route('/booking', methods=['GET'])
def get_booking_ids():
    # 返回所有 booking id
    return jsonify([{"bookingid": bid} for bid in bookings.keys()])

@app.route('/booking', methods=['POST'])
def create_booking():
    global next_id
    body = request.get_json()
    booking_id = next_id
    next_id += 1
    bookings[booking_id] = body  # 存储完整的请求体
    return jsonify({"bookingid": booking_id, "booking": body})

@app.route('/booking/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    if booking_id in bookings:
        return jsonify(bookings[booking_id])
    return "", 404

@app.route('/booking/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    token = request.cookies.get('token')
    if token != "mock-token-abc123":
        return "", 403
    if booking_id not in bookings:
        return "", 404
    body = request.get_json()
    bookings[booking_id] = body
    return jsonify(body)

@app.route('/booking/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    token = request.cookies.get('token')
    if token != "mock-token-abc123":
        return "", 403
    if booking_id in bookings:
        del bookings[booking_id]
    return "", 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

