import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data = pd.read_csv('orders_users_created_on_enero_2018_11_20.csv')

time_order = data['created_at']
time_order = [element[11:-6] for element in time_order]

price_order = data['total_price']
tip_by_order = data['tip']


data_1 = time_order
data_2 = price_order

short_data_1 = []
short_data_2 = []

count = 0
for index, val in enumerate(time_order):
    if count == 300:
        break
    print(data_1[index], data_2[index])
    short_data_1.append([data_1[index]])
    short_data_2.append([data_2[index]])
    count += 1

plt.figure(figsize=(8, 6))
plt.scatter(short_data_1, short_data_2, marker='_', color='red')
plt.show()

