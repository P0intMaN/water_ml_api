# MODEL CREATION
# imports
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import pickle


# # load dataset
# dataset = pd.read_csv('water_potability.csv')
# dataset.head()

# dataset.isna().sum()

# # dropping NAN and NULLS
# dataset.dropna(inplace=True)
# dataset

# dataset.isna().sum()

# # selecting features
# X = dataset[['ph', 'Hardness', 'Turbidity', 'Temperature']]
# X

# # labels
# y = dataset.iloc[:, -1]
# y

# # split the dataset into x_train, x_test, y_train, y_test ([x=independent, y=target)
# from sklearn.model_selection import train_test_split

# x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2, stratify=y)

# #feature scaling
# from sklearn.preprocessing import StandardScaler

# sc=StandardScaler()
# x_train_sc=sc.fit_transform(x_train)
# x_test_sc=sc.fit_transform(x_test)

# # testing SVM
# from sklearn import svm

# classifier = svm.SVC(kernel='rbf')
# classifier.fit(x_train_sc,y_train)

# # save model
# file_name = 'water_quality_svm.sav'
# pickle.dump(classifier, open(file_name, 'wb'))

# # prediction
# preds = classifier.predict(x_test_sc)

# #accuracy checking
# from sklearn.metrics import accuracy_score

# # pass the training data and target variable
# print(accuracy_score(preds,y_test))

# # load later....
# # loaded_model = pickle.load(open(file_name, 'rb'))
# # result = loaded_model.score(X_test, Y_test)
# # print(result)




# APPLICATION INTERFACE
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
