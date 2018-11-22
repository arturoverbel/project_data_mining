import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data = pd.read_csv('orders_users_created_on_enero_2018_11_20.csv')
time_order = data['created_at']
price_order = data['total_price']

time_order = [element[11:-6] for element in time_order]

short_data_1 = []
short_data_2 = []

count = 0
for index, val in enumerate(time_order):
    if count == 300:
        break
    print(time_order[index], price_order[index])
    short_data_1.append([time_order[index]])
    short_data_2.append([price_order[index]])
    count += 1

plt.figure(figsize=(8, 6))
plt.scatter(short_data_1, short_data_2, marker='_', color='red')
plt.show()

