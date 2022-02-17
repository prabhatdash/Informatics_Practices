#AIM-WAPP to create a dictionary which will store the first name n no. of students and the last name of n no. of students in another dictionary.
    #After creating the dictionary do the following--
   #1-Update the last name of any key
   #2-Delete any one of the first name
   #3-print all the key of the dictionary storing first name
   #4-print all the value of the dictionary storing last name

n=int(input("enter the no. of students"))
f_name={}
l_name={}
for i in range(0,n):
    k=int(input("enter the serial no. of students"))
    pp=input("enter the first name of students")
    o=input("enter the last name of student")

    f_name[k]=pp
    l_name[k]=o

    print(f_name)
    print(l_name)

    c=int(input("enter the serial no. of student of whom you want to change the last name"))
    e=input("enter the new last name students")

    l_name[c]=e
    print(l_name)
    len1=len(f_name)
    len2=len(l_name)
    print("total no. ")
