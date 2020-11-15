#Filename: Central Limit Theorem
#Author: Kyle Larson
#Purpose: To demonstrate the central limit theorem
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)
#note to self install pandas as soon as possible
#help(np.random)

#TO DO ---------------------------------
#Demonstrate the central limit theorem
#Generate random numbers()
#in a matrix of 900 elements
#perform a mean of every row
#plot each of the means in a histogram
#
#Demonstrate the face splitting product
#
#Calculate the number of weeks in 100 days
#rds = np.random.rand(300, 300)
#print(rds)
#print(np.random(1))