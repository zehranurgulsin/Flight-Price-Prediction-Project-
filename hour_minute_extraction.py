import pandas as pd
 
train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()
def extract_hour_min(df, col):
    df[col + "_hour"] = df[col].dt.hour
    df[col + "_minute"] = df[col].dt.minute
    return df.head(3)

# Extract hour and minute information from 'Dep_Time' and 'Arrival_Time' columns
print(data.columns)
print(extract_hour_min(data, "Dep_Time"))
print(extract_hour_min(data, "Arrival_Time"))
cols_to_drop = ['Arrival_Time', "Dep_Time"]
data.drop(cols_to_drop, axis=1, inplace=True)
print(data.head(3))
print(data.shape)
