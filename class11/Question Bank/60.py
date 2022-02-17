#AIM-to take the percentage of the student as an input from the user and display the details accordingly

data={}
std=int(input("ENTER THE NO OF STUDENTS"))
for i in range(0,std):
    print("ENTER THE STUDENT NAME")
    NAME=(input())
    print("ENTER THE PERCENTAGE OF STUDENT",NAME,":")
    marks = int(input())
    data[NAME]=marks

print(data)
