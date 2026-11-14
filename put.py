from flask import Flask, request, jsonify, abort
from routes import routes

app = Flask(__name__)

@app.route("/api/v1/routes/update/<route_number>", methods=['PUT'])
def update_route(route_number):
    #Send a request for the JSON file
    data = request.get_json()

    #Detects if "data" is empty, returns code 400 if data is empty
    if not data:
        abort(400, description="No provided data for update") #Stops the API request immediately and returns HTTPException

    for route in routes:
        if route["route_number"] == route_number:
            route.update(data)
            return jsonify({
                "message": f"Route {route_number} updated successfully",
                "route": route
            })
    abort(404, description="Route unavailable") #Error message if requested route number doesn't exist

if __name__ == "__main__":
    app.run(debug=True)