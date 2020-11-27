# YOU CAN IGNORE THIS FILE

from flask import Flask

from challenge import api
from challenge.extensions import db, migrate


def create_app(testing=False, cli=False):
    """Application factory, used to create application"""
    app = Flask("challenge")
    app.config.from_object("challenge.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_extensions(app, cli):
    """configure flask extensions"""
    db.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(api.views.blueprint)
