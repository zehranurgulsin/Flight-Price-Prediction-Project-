import pandas as pd
import seaborn as sns
train_data = pd.read_excel(r"C:\Users\\Desktop\Flight_Price_resources\Datasets\Data_Train.xlsx")

data = train_data.copy()
def preprocess_duration(x):
    if 'h' not in x:
        x = '0h' + ' ' + x
    elif 'm' not in x:
        x = x + ' ' + '0m'
    return x

data['Duration'] = data['Duration'].apply(preprocess_duration)
print(data['Duration'])

data['Duration_hours'] = data['Duration'].apply(lambda x: int(x.split(' ')[0][0:-1]))
data['Duration_mins'] = data['Duration'].apply(lambda x: int(x.split(' ')[1][0:-1]))

# Calculate total duration in minutes
data['Duration_total_mins'] = data['Duration'].str.replace('h', "*60").str.replace(' ', ' + ').str.replace('m', "*1").apply(eval)

print(data.columns)
print(sns.scatterplot(x="Duration_total_mins", y="Price", data=data))
print(sns.scatterplot(x="Duration_total_mins", y="Price", hue="Total_Stops", data=data))
print(sns.lmplot(x="Duration_total_mins", y="Price", data=data))
