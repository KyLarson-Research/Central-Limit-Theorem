#Filename: Central Limit Theorem
#Author: Kyle Larson
#Purpose: To demonstrate the central limit theorem
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#note to self install pandas as soon as possible
#help(np.random)

#TO DO ---------------------------------
#Demonstrate the central limit theorem
#Generate random numbers()
#in a matrix of 900 elements
#perform a mean of every row
#plot each of the means in a histogram
x = []
rds = np.random.rand(300, 300)
for i in range(len(rds[0])):
	x.append(np.mean(rds[i]))

plt.hist(x)
plt.show()