#Aim: Write a program to calculate the total points earned by both the teams in each round

import pandas as pd
round1_data={'team1':[10,20,30,40],'team2':[15,16,17,18]}
round1df=pd.DataFrame(round1_data)
print("Round 1 Performance of Both Team:")
print(round1df)
round2_data={'team1':[11,21,31,41],'team2':[16,17,18,19]}
round2df=pd.DataFrame(round2_data)
print("Round 2 Performance of Both Team:")
print(round2df)

print("Total Points Earned By Both Team:")
print(round1df+round2df)