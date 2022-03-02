#Marks is a list that stores marks of a student in 10 unit test. Write a program to plot the student's performance in these 10 unit tests.

import matplotlib.pyplot as plt
week=[1,2,3,4,5,6,7,8,9,10]
marks=[12,10,10,15,17,16,18,14,16,13]
plt.plot(week,marks)
plt.xlabel("WEEK")
plt.ylabel("MARKS")
plt.savefig('2.png')
plt.show()