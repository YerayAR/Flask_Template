"""Flask application factory and extension initialization."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

# Initialize extensions

# SQLAlchemy instance used for all database interactions
db = SQLAlchemy()
# Handles user session management for authentication
login_manager = LoginManager()
# Provides CSRF protection for forms
csrf = CSRFProtect()

# Application factory

def create_app(config_class=Config):
    """Application factory used by Flask to create instances."""

    # Create Flask application and load configuration
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions with the application instance
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    # Redirect unauthorized users to the login page
    login_manager.login_view = 'auth.login'

    # Register blueprint containing authentication views
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    # Register blueprint containing main application routes
    from .main import main_bp
    app.register_blueprint(main_bp)

    return app

# Import models so that Flask-SQLAlchemy can locate them
from . import models
