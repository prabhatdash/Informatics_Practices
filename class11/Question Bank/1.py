# TO CALCULATE THE AREA OF FOLLOWING-
#1.TRIANGLE
#2.TRAPIZIUM
#3.SECTOR OF circle

print('enter the base of triangle')
base=float(input())
print('enter the height of triangle')
height=float(input())
area=1/2*base*height
print(area)

print('enter the 1st side of triangle')
first_side=float(input())
print('enter the 2nd side od trapizium')
second_side=float(input())
print('enter the Height')
Height=float(input())
area_of_trapizium=first_side+second_side/2*Height
print(area_of_trapizium)

print('enter the angle')
angle=float(input())
pie=22/7
print('enter the radius')
r=float(input())
sector_of_circle=angle/360*pie*r*r
print(sector_of_circle)
