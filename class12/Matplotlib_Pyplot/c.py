#Write a program to plot a horizontal bar chart from the heights of some students.

import matplotlib.pyplot as plt
heights=[5.1,5.5,6.0,5.0,6.3]
names=['Asma','Bela','Chris','Diya','Saqib']
plt.barh(names,heights)
plt.xlabel("HEIGHTS")
plt.ylabel("NAMES")
plt.show()