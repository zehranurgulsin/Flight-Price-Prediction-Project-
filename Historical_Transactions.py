import pandas as pd

train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()

print(data.columns)
print(data.head(2))
print(data.dtypes)

def change_into_Datetime(col):
    data[col] = pd.to_datetime(data[col])

import warnings
warnings.filterwarnings("ignore")

for feature in ['Dep_Time', 'Arrival_Time', 'Date_of_Journey']:
    change_into_Datetime(feature)

data["Journey_day"] = data['Date_of_Journey'].dt.day
data["Journey_month"] = data['Date_of_Journey'].dt.month
data["Journey_year"] = data['Date_of_Journey'].dt.year
print(data.head(3))
