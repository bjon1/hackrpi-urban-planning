from flask import Flask, jsonify, request
from coordinator import Coordinator

app = Flask(__name__)
coordinator : Coordinator = Coordinator()

@app.route('/get/map')
def get_map():
    map = coordinator.get_map()
    return jsonify(map), 200

@app.route('/check_radius_explored', methods=['GET'])
def check_radius_explored():
    # Get coordinates and radius from query parameters
    coordinates_str = request.args.get('coordinates')  # e.g., "10,20"
    radius = request.args.get('radius', default=10, type=int)

    # Check if coordinates were provided
    if not coordinates_str:
        return jsonify({"error": "Missing 'coordinates' parameter"}), 400

    # Parse coordinates string into a list of integers
    try:
        coordinates = [int(x) for x in coordinates_str.split(",")]
        if len(coordinates) != 2:
            raise ValueError("Coordinates must have exactly two values.")
    except ValueError:
        return jsonify({"error": "Invalid 'coordinates' format. Expected format: 'x,y'."}), 400

    # Call the check_radius_explored method and return results
    updated_list = coordinator.check_radius_explored(coordinates, radius)
    return jsonify(updated_list), 200