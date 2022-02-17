#to find the area of a triangle and see if its area is even or odd

H=int(input("enter the height of the triangle:"))
B=int(input("enter the base of the triangle:"))
area=1/2*(B*H)
print("area",area)

if area%2==0:
	print("area of the triangle is even")
if area%2!=0:
	print("area of the triangle is odd")
else:
	print("error")