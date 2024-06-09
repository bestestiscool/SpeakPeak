from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """User in the system."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relationship to search history
    search_histories = db.relationship('SearchHistory', backref='user', lazy=True)


class Word(db.Model):
    """Word in the dictionary."""
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False, unique=True)
    pronunciations = db.relationship('Pronunciation', backref='word', lazy=True)
    translations = db.relationship('Translation', backref='word', lazy=True)

class Pronunciation(db.Model):
    """Pronunciation of a word."""
    __tablename__ = 'pronunciations'
    
    id = db.Column(db.Integer, primary_key=True)
    audio_url = db.Column(db.Text, nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)

class Translation(db.Model):
    """Translation of a word in a different language."""
    __tablename__ = 'translations'
    
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(50), nullable=False)
    translation = db.Column(db.String(120), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)

class GuestSession(db.Model):
    """Session for a guest user."""
    __tablename__ = 'guest_sessions'
    
    id = db.Column(db.String(120), primary_key=True)  # Session token
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

class SearchHistory(db.Model):
    """Record of a search made by a user or guest."""
    __tablename__ = 'search_history'
    id = db.Column(db.Integer, primary_key=True)
    searched_word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_session_id = db.Column(db.String, db.ForeignKey('guest_sessions.id'), nullable=True)
    
    search_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    # Add relationship to Word model
    word = db.relationship('Word', backref='search_histories', lazy=True)
    
def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)
    db.create_all()
