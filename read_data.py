import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

FEATURE1 = 'rapida'
FEATURE2 = 'mercados'
FEATURE3 = 'vegetariana'
FEATURE4 = 'oriental'
FEATURE5 = 'licores'
FEATURE6 = 'tecnologia'

FEATURE_TARGET = 'class'

FILE_NAME = 'dataByUser3.csv'

# Set data from file
df = pd.read_csv(FILE_NAME)
target = df[FEATURE_TARGET]

x = df[FEATURE1]
y = df[FEATURE2]
z = df[FEATURE3]
z1 = df[FEATURE4]
z2 = df[FEATURE5]
z3 = df[FEATURE6]

Y = []
X = []

class_all_x = []
class_all_y = []

for idx, val in enumerate(target):

    data_x = float(x[idx])
    data_y = float(y[idx])
    data_z = float(z[idx])
    data_z1 = float(z1[idx])
    data_z2 = float(z2[idx])
    data_z3 = float(z3[idx])

    Y.append(val)
    X.append([data_x, data_y, data_z, data_z1, data_z2, data_z3])
    class_all_x.append(data_x)
    class_all_y.append(data_y)

# Shuffle and split the data into training and test set
X, Y = shuffle(X, Y)
x_train = []
y_train = []
x_test = []
y_test = []

porcent = 90

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=porcent/100)



len_total = len(X)
len_dataset_train = len(x_train)

# Example data
data_train = np.array(x_train)
# Label
label_train = np.array(y_train)
data_test = np.array(x_test)
label_test = np.array(y_test)

label_train = label_train.reshape(len_dataset_train, 1)
label_test = label_test.reshape(len_total-len_dataset_train, 1)

data_train_x = data_train[:, 0]
data_train_y = data_train[:, 1]

data_train_x = data_train_x.reshape(len_dataset_train, 1)
data_train_y = data_train_y.reshape(len_dataset_train, 1)

clf = SVC(kernel='linear')

#x_train = [[0, 0], [1, 1]]
#y_train = [0, 1]

print(x_train)
print(y_train)
model = clf.fit(x_train, y_train)
print(model)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))


plt.figure(figsize=(8, 6))
plt.scatter(class_all_x, class_all_y, marker='+', color='blue')

plt.show()