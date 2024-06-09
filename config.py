# createdb speakpeak_test

# export TEST_DATABASE_URL=postgresql:///speakpeak_test



import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "it's a secret")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql:///speakpeak')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_ENABLED = False
    MW_API_KEY = os.getenv('MW_API_KEY')
    MW_API_BASE_URL = os.getenv('MW_API_BASE_URL', 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/')
    
    if not MW_API_KEY:
        raise ValueError("No MW_API_KEY set for Flask application. Please set the environment variable MW_API_KEY.")


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql:///test_speakpeak')  # Use a separate test database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    DEBUG = False
