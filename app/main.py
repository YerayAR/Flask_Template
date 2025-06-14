from flask import Blueprint, render_template, redirect, url_for, jsonify
from .forms import ContactForm
from .models import Contact
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        entry = Contact(name=form.name.data, email=form.email.data,
                        message=form.message.data)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('contact.html', form=form)

@main_bp.route('/api/contacts')
def api_contacts():
    contacts = Contact.query.all()
    data = [{'id': c.id, 'name': c.name, 'email': c.email, 'message': c.message}
            for c in contacts]
    return jsonify(data)
