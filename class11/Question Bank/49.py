#AIM- to calculate the vowels in a string

vowels=['a','e','i','o','u']
count=0
a=input('enter something')
for i in a:
    if i in vowels:
        count+=1
print(count)
