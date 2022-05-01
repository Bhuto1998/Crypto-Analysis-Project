import numpy as np
from sklearn_som.som import SOM
from sklearn import datasets
import matplotlib.pyplot as plt
import rand as rand

m = 10#35
n = 10#29
# Number of training examples
n_x = 30000
rand = np.random.RandomState(0)
# Initialize the training data
train_data = np.random.uniform(0, 1, (n_x,2))
# Initialize the SOM randomly
#s = [10,10,2]
#SOM = np.random.uniform(0.3,0.7,s)
SOM_model = SOM(m=5,n=5,dim = 2)

data = []

data = []
for i in range(len(SOM_model.cluster_centers_)):
    for j in range(len(SOM_model.cluster_centers_[0])):
        data = data + [SOM_model.cluster_centers_[i][j]]
data_2d = np.stack(data)
plt.scatter(data_2d[:,0],data_2d[:,1])
plt.savefig("fig_final_weight.png")
#print("debug")



