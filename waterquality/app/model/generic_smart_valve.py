import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import pickle

datasets = [
    "monday_dataset", 
    "tuesday_dataset", 
    "wednesday_dataset", 
    "thursday_dataset", 
    "friday_dataset", 
    "saturday_dataset", 
    "sunday_dataset"
]

svm_machine_pool = []

def train_svm(df, index):

    x = df.drop("Flow Rate", axis=1)
    y = df.iloc[:,1]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # data pre-processing
    # standard scaling the dataset
    # sc = StandardScaler()
    # x_train_sc = sc.fit_transform(x_train)
    # x_test_sc = sc.fit_transform(x_test)

    # fit the SVR model
    regressor = SVR(kernel='rbf')
    regressor.fit(x_train, y_train)

    svm_machine_pool.append(regressor)
    pickle.dump(regressor, open(f'generic_svm_model_{index}.sav', 'wb'))

def is_leakage(day_format, flow_rate, time, water_pressure):
    projection = svm_machine_pool[day_format].predict([
        [
            time,
            water_pressure
        ]
    ])

    projection += 0.3

    if flow_rate > projection:
        return 1, projection
    else:
        return 0, projection


def is_leakage_model(day_format, flow_rate, time, water_pressure):
    projection = svm_machine_pool[day_format].predict([
        [
            time,
            water_pressure
        ]
    ])

    projection += 0.3

    if flow_rate > projection:
        return 1, projection
    else:
        return 0, projection



# preparing the datasets
dataframes = []
for name in datasets:
    dataframes.append(pd.read_csv(f"dataset/{name}.csv"))

for index, df in enumerate(dataframes):
    train_svm(df, index)


print(is_leakage(day_format=0, flow_rate=3.5, time=8, water_pressure=240))
# DETECTS BOTH MINUTE AND LARGE LEAKS

# calling the correct serialized model 
# based on the day_format

is_leakage_model(day_format=0, flow_rate=3.5, time=6, water_pressure=240)
