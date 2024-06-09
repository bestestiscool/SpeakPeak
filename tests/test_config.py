import os

def test_config():
    """
    Test configuration settings
    """
    from app import create_app
    app = create_app('testing')
    assert app.config['DEBUG'] is False
    assert app.config['TESTING'] is True
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('TEST_DATABASE_URL', 'postgresql:///speakpeak_test')
