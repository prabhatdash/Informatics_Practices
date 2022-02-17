#TO CHECK IF THE FIRST LETTER OF A NAME HAS A VOWEL OR NOT.
print('enter the name')
name=input()
vowels=['a','e','i','o','u']
if name[0] in vowels:
    print('yeah')
else:
    print("nope")