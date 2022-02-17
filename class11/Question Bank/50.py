#AIM-to check the no. of even no.s in digit
d=input("Enter the digit:")
count=0
for i in d:
    if int(i)%2==0:
        count+=1
print("total number of even characters in the digit:",count)
        