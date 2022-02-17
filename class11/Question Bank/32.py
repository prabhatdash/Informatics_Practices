#take three numbers as input from the user and check the greatest of them.

f=int(input("enter first number:"))
s=int(input("enter second number:"))
l=int(input("enter third number:"))
if f>s and f>l:
	print("first number is greater")
elif s>f and s>l:
	print("second number is greater")
else:
	print("third number is greater")