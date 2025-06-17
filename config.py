"""Configuration values for the Flask application."""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration with sensible defaults."""

    # Secret key used for sessions and CSRF tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Database URL can be provided via environment variable, fallback to SQLite
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    # Disable tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
