from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controllers import HomeController, HealthController, AboutController

# init server
app = Flask(__name__)
api = Api(app)

# cors origins
CORS(app)

# route
api.add_resource(HomeController, "/")
api.add_resource(HealthController, "/health")
api.add_resource(AboutController, "/about")

if __name__ == "__main__":
    app.run(debug=True)
