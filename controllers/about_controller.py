from flask import request, jsonify
from flask_restful import Resource

class AboutController(Resource):
    def get(self):
        return jsonify({
            "message": "about service..."
        })