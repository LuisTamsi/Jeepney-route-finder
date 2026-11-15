from flask import Blueprint, request, jsonify
from routes import routes

bp = Blueprint("post", __name__)

@bp.route('/api/v1/routes/create/<route_id>', methods=['POST'])
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
    bp.run(debug=True)