#TO FIND THE NUMBER OF FRIENS WHO HAVE EVEN CHARACTERS IN THEIR NAME
n=int(input("ENTER NUMBER OF FRIENDS:"))
c=0
f=0
for i in range(0,n):
	k=input("ENTER NAME OF FRIEND:")
	s=len(k)
	if s%2==0:
		c+=1
	else:
		f+=1
print("number of even names:",c)
print("number of odd names:",f)
		