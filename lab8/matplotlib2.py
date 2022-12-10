import matplotlib.pyplot as plt
import numpy as np

y = np.array([45, 20, 25, 10])
mylabels = ["Vară", "Toamnă", "Iarnă", "Primăvară"]
mycolors = ["#fffcc3", "#560000", "#81a7b2", "#d9a7b2"]
myexplode = [0.2, 0, 0, 0]
plt.title("Anotimpuri preferate", loc = 'left')

plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode, shadow = True) #piechart
plt.show()