from flask import render_template
from app import flask_app
import pickle
from flask import request

@flask_app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

water_quality = pickle.load(open(r"water_quality_svm.sav", 'rb'))
sc = pickle.load(open(r"sc.pkl", 'rb'))
le = pickle.load(open(r"le.pkl", 'rb'))
water_pressure = pickle.load(open(r"water_pressure.sav", 'rb'))

# creating route
@flask_app.route("/predict")
def prediction():
    ph = float(request.args.get("ph"))
    hardness = float(request.args.get("hardness"))
    temperature = float(request.args.get("temperature"))
    turbidity = float(request.args.get("turbidity"))
    vp = float(request.args.get("valvepressure"))
    pred1 = str(water_quality.predict(sc.transform([[ph, hardness, temperature, turbidity]])))
    pred2 = str(le.inverse_transform(water_pressure.predict([[vp]])))
    return str(pred1 + " " + pred2)
