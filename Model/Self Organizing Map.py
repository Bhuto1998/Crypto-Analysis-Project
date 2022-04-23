import numpy as np
import matplotlib.pyplot as plt

#Algorithm
# Initialize Grid weight
# Repeat until convergence or max epoch
#  run over all datapoint in each epoch
#  For each data x
#  Find best matching unit
#  Update weight vector of bmu and other cells

#We will use random intitialization

#Function to find best matching unit: returns g,h -> co-ordinate of best matching unit
import rand as rand


def Best_Matching(SOM,x):
    temp = (np.square(SOM-x)).sum(axis=2)
    return np.unravel_index(np.argmin(temp, axis=None), temp.shape)

def Weight_Update(SOM,train_ex,learn_rate,radius_sq,BMU_coord,step=3):
    g, h = BMU_coord
    # if radius is close to zero then only BMU is changed
    if radius_sq < 1e-3:
        SOM[g, h, :] += learn_rate * (train_ex - SOM[g, h, :])
        return SOM
    # Change all cells in a small neighborhood of BMU
    for i in range(max(0, g - step), min(SOM.shape[0], g + step)):
        for j in range(max(0, h - step), min(SOM.shape[1], h + step)):
            dist_sq = np.square(i - g) + np.square(j - h)
            dist_func = np.exp(-dist_sq / 2 / radius_sq)
            SOM[i, j, :] += learn_rate * dist_func * (train_ex - SOM[i, j, :])
    return SOM


# Main routine for training an SOM. It requires an initialized SOM grid
# or a partially trained grid as parameter
def train_SOM(SOM, train_data, learn_rate = .1, radius_sq = 1,
             lr_decay = .1, radius_decay = .1, epochs = 10):
    learn_rate_0 = learn_rate
    radius_0 = radius_sq
    for epoch in np.arange(0, epochs):
        rand.shuffle(train_data)
        for train_ex in train_data:
            g, h = Best_Matching(SOM, train_ex)
            SOM = Weight_Update(SOM, train_ex,
                                 learn_rate, radius_sq, (g,h))
        # Update learning rate and radius
        learn_rate = learn_rate_0 * np.exp(-epoch * lr_decay)
        radius_sq = radius_0 * np.exp(-epoch * radius_decay)
    return SOM

#Experiment
# Dimensions of the SOM grid
m = 35
n = 29
# Number of training examples
n_x = 30000
rand = np.random.RandomState(0)
# Initialize the training data
train_data = rand.randint(0, 255, (n_x, 3))
# Initialize the SOM randomly
SOM = rand.randint(0, 255, (m, n, 3)).astype(float)
# Display both the training matrix and the SOM grid
fig, ax = plt.subplots(
    nrows=1, ncols=2, figsize=(12, 3.5),
    subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(train_data.reshape(500, 60, 3))
ax[0].title.set_text('Training Data')
ax[1].imshow(SOM.astype(int))
ax[1].title.set_text('Randomly Initialized SOM Grid')
plt.savefig("Initial.png")

#Training Process
fig, ax = plt.subplots(
    nrows=1, ncols=4, figsize=(15, 3.5),
    subplot_kw=dict(xticks=[], yticks=[]))
total_epochs = 0
for epochs, i in zip([1, 4, 5, 10], range(0,4)):
    total_epochs += epochs
    SOM = train_SOM(SOM, train_data, epochs=epochs)
    ax[i].imshow(SOM.astype(int))
    ax[i].title.set_text('Epochs = ' + str(total_epochs))
    plt.savefig("Epoch-"+str(total_epochs)+".png")
    print("Saved")


