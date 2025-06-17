"""Entry point for running the Flask development server."""

from app import create_app, db
from app.models import User, Contact

# Create the Flask application instance
app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Automatically import objects when using the Flask shell."""

    return {'db': db, 'User': User, 'Contact': Contact}

if __name__ == '__main__':
    # Launch the built-in development server
    app.run()
