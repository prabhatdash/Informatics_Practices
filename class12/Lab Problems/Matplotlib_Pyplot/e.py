# Create multiple line charts on common plot where three data ranges are plotted on same charts. The data ranges to be plotted is/are:
#data=[[5.,25.,45.,20.],[8.,13.,29.,27.],[9.,29.,27.,39.]]

import numpy as np
import matplotlib.pyplot as plt
data=[[5.,25.,45.,20.],[8.,13.,29.,27.],[9.,29.,27.,39.]]
x=np.arange(4)
plt.plot(x,data[0],color='r',label='range1')
plt.plot(x,data[1],color='b',label='range2')
plt.plot(x,data[2],color='g',label='range3')
plt.legend(loc='upper left')
plt.title("MultiRange Line Chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()