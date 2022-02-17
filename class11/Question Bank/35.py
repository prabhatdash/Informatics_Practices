#TO CHECK IF A NUMBER IS ARMSTRONG OR NOT
a=input("ENTER NUMBER:")
x=int(a)
b=len(a)
c=int(b)
sum=0
for i in range(0,c):
	d=int(a[i])**c
	sum+=d
if sum==x:
	print("THE NUMBER IS ARMSTRONG")
else:
	print("THE NUMBER IS NOT ARMSTRONG")