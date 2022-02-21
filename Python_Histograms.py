# https://www.w3schools.com/python/matplotlib_histograms.asp
# Histograms
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(200, 10, 680)
print (x) 

plt.hist(x)
plt.show()