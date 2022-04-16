from flask import render_template
from app import flask_app

@flask_app.route('/')
def home():
    return render_template('home.html')
