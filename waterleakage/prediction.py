import pickle
# import pandas as pd

# # load the dataset
# df = pd.read_csv("leakage_dataset.csv")

# # remove missing value rows
# df.dropna(inplace=True)

# # label encoding the output column
# from sklearn.preprocessing import LabelEncoder
# le= LabelEncoder()
# y_encoded=le.fit_transform(df["leakage"])

# # creating train values
# X = df["valve pressure"].values.reshape(-1,1)

# # train test split
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test= train_test_split(X,y_encoded,test_size=0.2)

# # logistic regression for multiple label classification
# from sklearn.linear_model import LogisticRegression
# clf = LogisticRegression(random_state=0).fit(X_train, y_train)
# pickle.dump(le, open("le.pkl", "wb"))
# pickle.dump(clf, open("savedmodel.sav", "wb"))

# # predicting output
# print(le.inverse_transform(clf.predict([[700]])))

model = pickle.load(open("savedmodel.sav", "rb"))
le = pickle.load(open("le.pkl", "rb"))
print(le.inverse_transform(model.predict([[700]])))