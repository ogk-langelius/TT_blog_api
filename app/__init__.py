from flask import Flask, jsonify
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env=None):
    """Create an app using certain configuration."""
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or 'test'])
    api = Api(app, title='Flaskerific API', version='0.0.1')

    register_routes(api, app)
    db.init_app(app)

    return app
