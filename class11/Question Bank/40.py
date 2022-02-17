#TO CHECK IF THE NAME IS PALINDROM OR NOT
name=input("ENTER NAME:")
ultanaam=name[::-1]
if name==ultanaam:
	print("the name is palindrom")
else:
	print("it is not palindrom")