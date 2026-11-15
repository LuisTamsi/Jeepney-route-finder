from flask import Flask, request, jsonify

app = Flask(__name__)

routes = [
    {"route_number": "1", "origin": "Public Market", "destination": "City Hall", "fare": 13},
    {"route_number": "2", "origin": "Bus Terminal", "destination": "Public Market", "fare": 15},
    {"route_number": "3", "origin": "City Hall", "destination": "General Hospital", "fare": 13},
    {"route_number": "4", "origin": "Town Plaza", "destination": "Shopping Mall", "fare": 15},
    {"route_number": "5", "origin": "Public Market", "destination": "University", "fare": 13},
    {"route_number": "6", "origin": "Bus Terminal", "destination": "City Hall", "fare": 15},
    {"route_number": "7", "origin": "Shopping Mall", "destination": "General Hospital", "fare": 18},
    {"route_number": "8", "origin": "University", "destination": "Town Plaza", "fare": 13},
    {"route_number": "9", "origin": "Train Station", "destination": "Public Market", "fare": 15},
    {"route_number": "10", "origin": "Sports Complex", "destination": "Bus Terminal", "fare": 20},
    {"route_number": "11", "origin": "Airport", "destination": "City Center", "fare": 25},
    {"route_number": "12", "origin": "North Terminal", "destination": "South Station", "fare": 22},
    {"route_number": "13", "origin": "Port Area", "destination": "Public Market", "fare": 16},
    {"route_number": "14", "origin": "IT Park", "destination": "University", "fare": 14},
    {"route_number": "15", "origin": "Central Square", "destination": "Industrial Zone", "fare": 19}
]

@app.route('/api/v1/routes/create/<route_id>', methods=['POST'])
def add_route(route_id):
    data = request.get_json()

    for route in routes:
        if route["route_number"] == str(route_id):
            return jsonify({"error": f"Route {route_id} already exists"}), 400

    if not data or not all(key in data for key in ("origin", "destination", "fare")):
        return jsonify({"error": "Missing required fields: origin, destination, fare"}), 400

    new_route = {
        "route_number": str(route_id),
        "origin": data["origin"],
        "destination": data["destination"],
        "fare": data["fare"]
    }

    routes.append(new_route)
    return jsonify({
        "message": f"Route {route_id} added successfully",
        "route": new_route
    }), 201

if __name__ == '__main__':
    app.run(debug=True)