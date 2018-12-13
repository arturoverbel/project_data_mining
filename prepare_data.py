import numpy as np
import matplotlib.pyplot as plt

geohashesNorth = ['d2g6fe', 'd2g6fg', 'd2g6g5', 'd2g6g7', 'd2g6fd',
                  'd2g6ff', 'd2g6g4', 'd2g6g6', 'd2g6f9', 'd2g6fc',
                  'd2g6g1', 'd2g6g3', 'd2g6f8', 'd2g6fb', 'd2g6g0']

geohashesSouth = ['d2g6d9', 'd2g6dc', 'd2g6e1', 'd2g6dd', 'd2g6df',
                  'd2g6de', 'd2g6dg', 'd2g6e5', 'd2g6ds', 'd2g6du',
                  'd2g6eh', 'd2g6dt', 'd2g6dv', 'd2g6ej', 'd2g6dw']

producTypes = ['rapida', 'mercados', 'vegetariana', 'oriental', 'licores', 'tecnologia']
probabilitiesS = [0.4, 0.2, 0.2, 0.05, 0.1, 0.05]
probabilitiesN = [0.05, 0.3, 0.25, 0.25, 0.1, 0.05]
probabilitiesM = [0.4, 0.2, 0.2, 0.05, 0.1, 0.05]

genders = ['M', 'F']
paymentMethods = ['cash', 'datafono', 'credit', 'rappipay']

numberUsers = 100
numberOrders = np.arange(1500, 2000)

data = []
dataByUser = []

for userID in range(1, numberUsers+1):
    nOrders = np.random.choice(numberOrders, 1)[0]
    state = np.random.choice(2, 1)[0]
    gender = np.random.choice(genders, 1)[0]

    geohashes = []
    probabilities = []
    if state == 1:
        geohashes = geohashesNorth
        probabilities = probabilitiesN
    else:
        geohashes = geohashesSouth
        probabilities = probabilitiesS

    geohash = np.random.choice(geohashes, 1)[0]

    products = [0] * len(producTypes)

    for orderID in range(0, nOrders):
        product = np.random.choice(producTypes, 1, replace=False, p=probabilities)[0]

        order = [userID, gender, geohash, product]
        data.append(order)
        for idx, productOnList in enumerate(producTypes):
            if productOnList == product:
                products[idx] = products[idx] + 1

    dataResumenUser = [userID, gender, geohash, state, nOrders]

    productsNorm = products / np.linalg.norm(products)
    dataResumenUser.extend(productsNorm)

    dataByUser.append(dataResumenUser)

classA_x = []
classA_y = []
classB_x = []
classB_y = []

for idx, val in enumerate(dataByUser):
    if val[3] == 0:
        classA_x.append(val[5])
        classA_y.append(val[6])
    else:
        classB_x.append(val[5])
        classB_y.append(val[6])

for d in dataByUser:
    print(d)

plt.figure(figsize=(8, 6))
plt.scatter(classA_x, classA_y, marker='+', color='blue')
plt.scatter(classB_x, classB_y, marker='_', color='red')
plt.show()



