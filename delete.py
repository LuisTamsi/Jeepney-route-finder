from flask import Flask, request, jsonify
from routes import routes
app = Flask(__name__)

@app.route("/api/v1/routes", methods=["GET"]) 
def get_routes():
    return jsonify(routes), 200

if __name__ == "__main__":
    app.run(debug=True)