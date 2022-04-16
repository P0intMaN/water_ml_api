import pickle
from flask import Flask
from flask import request

# instancing app
app = Flask(__name__)

# loading the model
loaded_model = pickle.load(open("water_quality_svm.sav", 'rb'))
sc = pickle.load(open("sc.pkl", 'rb'))

# creating route
@app.route("/predict")
def prediction():
    ph = float(request.args.get("ph"))
    hardness = float(request.args.get("hardness"))
    temperature = float(request.args.get("temperature"))
    turbidity = float(request.args.get("turbidity"))
    preds = loaded_model.predict(sc.transform([[ph, hardness, temperature, turbidity]]))
    return str(preds)

app.run(debug=True)
