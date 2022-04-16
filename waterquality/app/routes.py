from flask import render_template
from app import flask_app
import pickle
from flask import request

@flask_app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

loaded_model = pickle.load(open(r"water_quality_svm.sav", 'rb'))
sc = pickle.load(open(r"sc.pkl", 'rb'))

# creating route
@flask_app.route("/predict")
def prediction():
    ph = float(request.args.get("ph"))
    hardness = float(request.args.get("hardness"))
    temperature = float(request.args.get("temperature"))
    turbidity = float(request.args.get("turbidity"))
    preds = loaded_model.predict(sc.transform([[ph, hardness, temperature, turbidity]]))
    return str(preds)
