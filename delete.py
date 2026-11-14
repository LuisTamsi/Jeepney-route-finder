from flask import Flask, request, jsonify
from routes import routes
app = Flask(__name__)

@app.route("/api/v1/routes/<route_number>", methods=["DELETE"])
def delete_route(route_number):
    for index, route in enumerate(routes):
        if route["route_number"] == route_number:
            routes.pop(index)
            return "", 204

    return jsonify({"error": "Route not found"}), 404