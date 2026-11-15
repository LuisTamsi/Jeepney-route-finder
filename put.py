from flask import Blueprint, request, jsonify, abort
from routes import routes

bp = Blueprint("put", __name__)

@bp.route("/routes/update/<route_number>", methods=['PUT'])
def update_route(route_number):
    #Send a request for the JSON file
    data = request.get_json()

    if not data:
        abort(400, description="No provided data for update")

    for route in routes:
        if route["route_number"] == route_number:
            route.update(data)
            return jsonify({
                "message": f"Route {route_number} updated successfully",
                "route": route
            })
    abort(404, description="Route unavailable")

if __name__ == "__main__":
    bp.run(debug=True)