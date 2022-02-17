#AIM-to store marks of student according to their roll no.s
data = {}
num_sub=int(input("enter the no. of subjects"))
for i in range(0,num_sub):
    roll = int(input("enter the roll no. of student:"))
    sub=int(input("enter the subject marks:"))
    data[roll]=sub
print("dictionary:",data)
