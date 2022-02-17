#take any 3 numbers from user and check if any of them is duplicate

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
 
if num1==num2 and num1!=num3:
 	print("number 1 and 2 are duplicate")
elif num2==num3 and num2!=num1:
 	print("number 2 and 3 are duplicate")
elif num3==num1 and num3!=num2:
 	print("number 3 and 1 are duplicate")
elif num1==num2 and num2==num3:
	print("all are duplicate")
else:
 	print("all are unique")