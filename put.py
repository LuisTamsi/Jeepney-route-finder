from flask import Blueprint, request, jsonify
from routes import routes, validate_route

bp = Blueprint("put", __name__)

@bp.route("/routes/update/<route_number>", methods=['PUT'])
@bp.route("/api/v1/routes/update/<route_number>", methods=['PUT'])
def update_route(route_number):
    data, error = validate_route(request.get_json(silent=True), partial=True)
    if error:
        return jsonify({"error": error}), 400

    for route in routes:
        if route["route_number"] == route_number:
            if 'route_number' in data and any(
                other is not route and other['route_number'] == data['route_number']
                for other in routes
            ):
                return jsonify({"error": "Route number already exists"}), 400
            route.update(data)
            return jsonify({
                "message": f"Route {route_number} updated successfully",
                "route": route
            })
    return jsonify({"error": "Route not found"}), 404

