import os
import pytest
from app import create_app, db
from dotenv import load_dotenv

# Load environment variables from .env.test
load_dotenv('.env.test')

@pytest.fixture(scope='module')
def test_client():
    """
    This fixture sets up a Flask test client for the entire test module.
    """
    app = create_app('testing')
    app.config.from_object('config.TestingConfig')
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
