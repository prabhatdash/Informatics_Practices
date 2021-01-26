#Aim: Write a python program to iterate over a dataframe containing names and marks, which then calculates grades as per marks (as per guidelines below) and adds them to the grade column.

# Marks > =90 grade A+
# Marks  70-90 grade A
# Marks 60-70 grade B
# Marks 50-60 grade C
# Marks 40-50 grade D
# Marks <40 grade E


import pandas as pd
data={'names':['a1','a2','a3','a4'],"marks":[60,90,50,40]}
df=pd.DataFrame(data)
grade=list()
for (i,j) in df.iterrows():
    if j['marks']>=90:
        grade.append("A+")
    elif j['marks'] >=70 and j['marks']<90:
        grade.append("A")
    elif j['marks'] >= 60 and j['marks'] < 70:
        grade.append("B")
    elif j['marks'] >= 50 and j['marks'] < 60:
        grade.append("C")
    elif j['marks'] >= 40 and j['marks'] < 50:
        grade.append("D")
    elif j['marks'] <40:
        grade.append("E")
    else:
        print("EXCEPTION")

df["grade"]=grade
print(df)