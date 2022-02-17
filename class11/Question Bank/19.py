#to take the number from user if the number is odd it should print the number is not divisible by 2 and if the number is even it should print number is divisible by 2 .If neither of them is satisfied print neither odd nor even.

number=int(input("enter a number:"))

if number%2!=0:
	print("number is not divisible by 2 ")
elif number%2==0:
	print("number is divisible by 2")
else:
	print("neither even nor odd")