print(__doc__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets

FEATURE1 = 'rapida'
FEATURE2 = 'tecnologia'
FEATURE3 = 'mercados'

FEATURE_TARGET = 'class'
CLASS_A = 1
CLASS_B = 0

FILE_NAME = 'dataByUser.csv'

# Set data from file
df = pd.read_csv(FILE_NAME)
target = df[FEATURE_TARGET]

x = df[FEATURE1]
yf = df[FEATURE2]

df = df.drop([FEATURE1, FEATURE2], axis=1)
y = []
X = []

for idx, val in enumerate(target):

    data_x = float(x[idx])
    data_y = float(yf[idx])

    if val == CLASS_A:
        y.append(-1)
    elif val == CLASS_B:
        y.append(1)
    X.append([data_x, data_y])


h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
lin_svc = svm.LinearSVC(C=C).fit(X, y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
titles = ['SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']


for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()