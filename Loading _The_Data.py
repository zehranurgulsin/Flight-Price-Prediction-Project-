import pandas as pd
import numpy as np

train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

print(train_data.head())
print(train_data.head(4))
print(train_data.info())
print(train_data.isnull().sum())
print(train_data['Total_Stops'])
print(train_data[train_data['Total_Stops'].isnull()])
train_data.dropna(inplace=True)
print(train_data.dtypes)
