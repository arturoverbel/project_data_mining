import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data = pd.read_csv('orders_users.csv')
lat = data['lat']
lng = data['lng']

count = 0
for index, val in enumerate(lat):
    if count == 100:
        break
    print(lat[index], lng[index])
    count += 1

plt.figure(figsize=(8, 6))
plt.scatter(lat, lng, marker='_', color='red')
plt.show()

