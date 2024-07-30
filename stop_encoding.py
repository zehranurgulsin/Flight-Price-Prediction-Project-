import pandas as pd
train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()
stop = {'non-stop': 0, '2 stops': 2, '1 stop': 1, '3 stops': 3, '4 stops': 4}
data['Total_Stops'] = data['Total_Stops'].map(stop)
