
#to calculate the area of 3 triangles and print the triangle with the highest area

h1=int(input("enter the height of triangle 1"))
b1=int(input("enter the bsse of triangle1"))
area1=h1*b1
print("area",area1)

h2=int(input("enter the height of triangle 2"))
b2=int(input("enter the bsse of triangle2"))
area2=h2*b2
print("area",area2)

h3=int(input("enter the height of triangle 3"))
b3=int(input("enter the bsse of triangle3"))
area3=h3*b3
print("area",area3)

if area1>area2 and area1>area3:
	print("triangle 1 has the laregest area")
elif area2>area1 and area2>area3:
	print("triangle 2 has the largest area")
elif area3>area1 and area3>area2:
	print("triangle 3 has largest area")