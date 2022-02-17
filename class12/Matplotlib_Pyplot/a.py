# Given the subject wise marks data, analyses the performance of the students subject wise by representing it into a bar chart.

import matplotlib.pyplot as plt
marks=[80,70,60,90,95]
subjects=["English","Maths","Physics","Chemistry","IP"]
plt.plot(subjects,marks,marker='o',color=['b','g','y','k'],label='marks')
plt.legend()
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS")
plt.show()
plt.savefig('abc.png')