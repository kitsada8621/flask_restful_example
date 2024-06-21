from flask import jsonify
from flask_restful import Resource


class HomeController(Resource):
    def get(self):
        return jsonify({
            "message": "Welcome to flask api"
        })
