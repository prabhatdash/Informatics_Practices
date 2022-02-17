#to find number of vowels in a string
ent=input("enter string:")
s=["a","e","i","o","u"]
d=0
for i in ent:
	if ent in s:
		d+=1
print("number of vowels:",d)
	