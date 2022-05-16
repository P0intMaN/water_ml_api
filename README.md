# Water Quality and Leakage Detection with SVM and Logistic Regressor (1-layer NN)
###### An inteface cum API which classifies whether the water quality is GOOD or BAD

## *Project Stack*
- **Web Technologies:** _Flask, JS, AJAX_
- **Machine Learning:** _Sklearn_
- **Core Concept:** _Support Vector Machine_, _Logistic Regression_

## *What is SVM?*
SVM stands for **Support Vector Machine** and is one of the premier **_supervised machine learning technique_** typically used for classification and regresion tasks. It is exceptionally known to find outliers and deal with them. SVM is highly effective when the **_dimensionality is huge_**. SVM also comes equipped with various **kernels** (we will be using **`rbf`** kernel) which facilitates learning from different types of datasets.

SVM learns by effectively drawing a **hyperplane** (a decision boundary) which tends to divide the datapoints. The hyperplane is drawn in such a fashion that the distances between
the respective datapoints of different classes are **maximum**.

![SVM in action](https://i.imgur.com/OUNcvwp.png)

## *The Approach*
- **Create a Web Interface:** Used **Flask** to create the entire backend. Also exposes a **`/predict`** API endpoint which would return `[1]` if the water quality is good otherwise `[0]`.
- **Data Preprocessing:** Preprocessed data to extract required attributes. Also implemented feature scaling with **_StandardScaler_** to encourage a better learning rate.
- **Training Model:** The model has been trained using a **SVM** with **rbf** kernel and a _stratified split_. The resultant model has been serialized using **`pickle`**.
- **Fetching Results:** The web interfaces makes an **AJAX** call to **`/predict` route with a GET request.** The model replies back with either `[1] or [0]`. `[1]` means water quality is **GOOD** else, **BAD**.
<div>
    
    
<div>
  
  <table>
  <tr>
    <td valign="top"><img align=top src="https://i.imgur.com/zY64MhV.png" width=95% ></td>
    <td valign="top"><img align=top src="https://i.imgur.com/vvymgNR.png" ></td>
  </tr>
</table>
    
## *Run Project 🚀*
To deploy the project in your local machine, go to **`water_quality_ml_api`** folder after downloading this project and follow the steps:

#### 1) Installing Dependencies
Open a terminal within the current working directory (inside **`water_quality_ml_api`**) and type:

```sh
$ pip install requirements.txt
```
#### 2) Run the Application
Now, go inside the **`waterquality`** folder and type the following in the terminal:

```sh
$ python run.py
```
You should get a confirmation on the terminal that **Running on: 127.0.0.1:5000**.

#### 3) View the Project
Go to your browser and enter: **`127.0.0.1:5000`** and you would find the project up and running!

## *View the Project Live 🛰️*
Go to [deployment site](https://water-quality-api.herokuapp.com/) and see the project in action!

## *Extended Support for Water Leakage Detection*
Now, the API is able to detect **water leakage** as well. It is trained on data sourced from **EPANET** software which simulated a single-valve pipeline distribution. The pressure metric is **barometer**
