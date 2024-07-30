import pandas as pd
train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()
cat_col = [col for col in data.columns if data[col].dtype == "object"]
num_col = [col for col in data.columns if data[col].dtype != "object"]

print(data['Source'].unique())

# Convert 'Source' column to dummy variables
for sub_category in data['Source'].unique():
    data['Source_' + sub_category] = data['Source'].apply(lambda x: 1 if x == sub_category else 0)

# Encode 'Airline' column based on average prices
airlines = data.groupby(['Airline'])['Price'].mean().sort_values().index
dict_airlines = {key: index for index, key in enumerate(airlines, 0)}
data['Airline'] = data['Airline'].map(dict_airlines)

# Replace 'New Delhi' with 'Delhi' in 'Destination' column
data['Destination'].replace('New Delhi', 'Delhi', inplace=True)
dest = data.groupby(['Destination'])['Price'].mean().sort_values().index
dict_dest = {key: index for index, key in enumerate(dest, 0)}
data['Destination'] = data['Destination'].map(dict_dest)
