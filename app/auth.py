"""Routes related to user authentication (login, logout, register)."""

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from .models import User
from . import db

# Blueprint grouping all authentication views under the prefix provided when
# registering in the application factory
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Authenticate a user and start a session."""

    form = LoginForm()
    if form.validate_on_submit():
        # Lookup user by username and verify the password
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        # Show error message if credentials are invalid
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    """Log the current user out and end the session."""

    logout_user()
    return redirect(url_for('main.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Create a new user account."""

    form = RegistrationForm()
    if form.validate_on_submit():
        # Create user record and store hashed password
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
