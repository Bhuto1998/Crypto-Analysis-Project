import numpy as np
from sklearn_som.som import SOM
from sklearn import datasets
import matplotlib.pyplot as plt
import rand as rand
iris = datasets.load_iris()
iris_data = iris.data[:,:2]
iris_label = iris.target

iris_som = SOM(m=3,n=2,dim = 2)
iris_som.fit(iris_data)
temp = iris_som.cluster_centers_[0][0]
temp2 = len(iris_som.cluster_centers_[0])
data = []
for i in range(len(iris_som.cluster_centers_)):
    for j in range(len(iris_som.cluster_centers_[0])):
        data = data + [iris_som.cluster_centers_[i][j]]
data_2d = np.stack(data)
plt.scatter(data_2d[:,0],data_2d[:,1])
plt.savefig("fig_trial.png")




