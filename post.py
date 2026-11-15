from flask import Flask, request, jsonify
from routes import routes

bp = Blueprint("post", __name__)

@app.route("/api/v1/routes/create/", methods=["POST"])
def create_route():
    data = request.get_json()

    if not data or not all(k in data for k in ("route_number", "origin", "destination", "fare")):
        return jsonify({"error": "Missing required fields"}), 400

    route_id = str(data["route_number"])

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

if __name__ == "__main__":
    app.run(debug=True)
