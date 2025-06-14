# Flask Example

This project is a small demonstration of a web application built with Flask. It
shows how to organize routes, templates, forms and a database using common
Flask extensions.

## Features

- SQLite database managed with SQLAlchemy
- Simple authentication with Flask-Login
- Contact form handled by Flask-WTF
- Bootstrap-based templates rendered with Jinja2
- API endpoint that returns contact data as JSON

## Setup

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Initialize the database:

```bash
flask shell -c "from app import db; db.create_all()"
```

4. Run the development server:

```bash
python run.py
```

Open `http://localhost:5000` in a browser to see the application.
