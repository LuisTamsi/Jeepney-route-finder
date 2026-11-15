from flask import Blueprint, request, jsonify
from routes import routes, validate_route

bp = Blueprint("post", __name__)

@bp.route("/api/v1/routes/create/", methods=["POST"])
def create_route():
    data, error = validate_route(request.get_json(silent=True))
    if error:
        return jsonify({"error": error}), 400

    route_id = data["route_number"]

    for r in routes:
        if str(r["route_number"]) == route_id:
            return jsonify({"error": f"Route {route_id} already exists"}), 400

    new_route = {
        "route_number": route_id,
        "origin": data["origin"],
        "destination": data["destination"],
        "fare": data["fare"]
    }

    routes.append(new_route)

    return jsonify({
        "message": f"Route {route_id} added successfully",
        "route": new_route
    }), 201

