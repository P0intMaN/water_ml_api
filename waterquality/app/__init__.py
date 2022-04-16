from flask import Flask

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = 'sh...-keep-this-a-secret'

from app import routes
