#to find the area of triangle and find the greatest area
b=float(input("enter breadth:"))
h=float(input("enter height:"))
area=1/2*(b*h)
print("area of 1st triangle:",area)
b1=float(input("enter breadth:"))
h1=float(input("enter height:"))
area2=1/2*(b1*h1)
print("area of 2nd triangle:",area2)
if area>area2:
	print("area of 1st triangle is greater")
else:
	print("area of 2nd triangle is greater")