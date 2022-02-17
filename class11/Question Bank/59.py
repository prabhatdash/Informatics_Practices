#AIM-to store marks of student according to their roll no.s
data={}
std=int(input("ENTER THE NO OF STUDENTS"))
for i in range(0,std):
    print("ENTER THE ROLL NO:")
    r_no=int(input())
    print("ENTER THE MARKS OF ROLL NO",r_no,":")
    marks = int(input())
    data[r_no]=marks

print(data)

x=int(input("enter the roll no."))
data[x]=int(input())
print(data)

