import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()
def plot(df, col):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    sns.displot(df[col], ax=ax1)
    sns.boxplot(df[col], ax=ax2)
    sns.displot(df[col], ax=ax3, kde=False)

print(plot(data, 'Price'))

q1 = data['Price'].quantile(0.25)
q3 = data['Price'].quantile(0.75)
iqr = q3 - q1
maximum = q3 + 1.5 * iqr
minimum = q1 - 1.5 * iqr
print(maximum)
print(minimum)

print([price for price in data['Price'] if price > maximum or price < minimum])
print(len([price for price in data['Price'] if price > maximum or price < minimum]))
data['Price'] = np.where(data['Price'] > 35000, data['Price'], maximum)
