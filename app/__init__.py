from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__, static_folder='static')

    if config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    elif config_name == 'production':
        app.config.from_object('config.ProductionConfig')
    elif config_name == 'development':
        app.config.from_object('config.DevelopmentConfig')
    else:
        raise ValueError(f"Unknown configuration: {config_name}")

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
