from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    if config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.Config')

    db.init_app(app)

    # Register blueprints
    from .routes import words_blueprint
    app.register_blueprint(words_blueprint)

    return app