from flask import render_template
from app import flask_app
from app.forms import WaterForm

@flask_app.route('/', methods=['GET', 'POST'])
def home():
    form = WaterForm()
    return render_template('home.html')

@flask_app.route('/predict')
def predict_model():
    return '[0]'
