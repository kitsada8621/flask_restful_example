from flask import jsonify
from flask_restful import Resource

class HealthController(Resource):
    def get(self):
        return jsonify({
            "message": "The server is running..."
        })