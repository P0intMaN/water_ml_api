from turtle import st
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
    day = float(request.args.get("day"))
    time = float(request.args.get("time"))
    fr = float(request.args.get("fr"))
    wp = float(request.args.get("wp"))
    pred1 = str(water_quality.predict(sc.transform([[ph, hardness, temperature, turbidity]])))
    pred3 = ""
    if day == 0:
        generic_svm = pickle.load(open(r"../generic_svm_model_0.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    elif day == 1:
        generic_svm = pickle.load(open(r"../generic_svm_model_1.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    elif day == 2:
        generic_svm = pickle.load(open(r"../generic_svm_model_2.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    elif day == 3:
        generic_svm = pickle.load(open(r"../generic_svm_model_3.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    elif day == 4:
        generic_svm = pickle.load(open(r"../generic_svm_model_4.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    elif day == 5:
        generic_svm = pickle.load(open(r"../generic_svm_model_5.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    elif day == 6:
        generic_svm = pickle.load(open(r"../generic_svm_model_6.sav", 'rb'))
        pred3 = float(generic_svm.predict([[time, wp]]))
    
    pred3 += 0.3
    if pred3 < fr:
        pred3 = "1"
    else:
        pred3 = "0"
        print(pred1, pred3)
    return str(pred1 + " " + pred3)
