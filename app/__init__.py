from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__, static_folder='static')

    if config_name == 'testing':
        load_dotenv('.env.test')  # Load test-specific environment variables
        app.config.from_object('config.TestingConfig')
    elif config_name == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    from app.words.routes import words_blueprint
    app.register_blueprint(words_blueprint, url_prefix='/words')

    # Register the home route
    @app.route('/')
    def home():
        from app.words.forms import WordForm
        form = WordForm()
        return render_template('home.html', form=form)

    return app
