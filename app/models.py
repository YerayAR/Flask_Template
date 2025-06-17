"""Database models used by the application."""

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager

class User(UserMixin, db.Model):
    """User account stored in the database."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        """Store a hashed version of the password."""

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Validate a password against the stored hash."""

        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    """Flask-Login user loader callback."""

    return User.query.get(int(user_id))

class Contact(db.Model):
    """Stored contact messages from the contact form."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
