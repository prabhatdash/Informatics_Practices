#TO CHECK IF THE INPUT STRING IS PALINDROME OR NOT.
print("enter the input")
k=input()
r_value=k[::-1]
if r_value==k:
    print("the entered value is palindrome")
else:
    print("this is not palindrome")
