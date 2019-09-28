from flask import Flask
from apis.api import api
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity



def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    CORS(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port='5000', debug=True)
