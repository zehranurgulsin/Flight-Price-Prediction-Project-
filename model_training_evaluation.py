import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()
x = data.drop(['Price'], axis=1)
y = data['Price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

m1_model = RandomForestRegressor()
m1_model.fit(x_train, y_train)
y_pred = m1_model.predict(x_test)

print(metrics.r2_score(y_test, y_pred))

# Model Performance Evaluation
def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

print(mape(y_test, y_pred))

def predict(ml_model):
    model = ml_model.fit(x_train, y_train)
    print('Training score : {}'.format(model.score(x_train, y_train)))
    y_prediction = model.predict
