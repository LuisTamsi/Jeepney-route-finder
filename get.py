from flask import Flask, request, jsonify
from routes import routes

app = Flask(__name__)

@app.route('/api/v1/routes', methods=['GET'])
def get_routes():
    return jsonify(routes), 200

@app.route('/api/v1/routes/<route_number>', methods=['GET'])
def get_routes_by_number(route_number):
    for route in routes:
        if route["route_number"] == route_number:
            return jsonify(route), 200
    return jsonify(error='Route not found'), 404 
                   
if __name__ == '__main__':
    app.run(debug=True)
