#TO CHECK IF A STATE EXIST IN A LIST OF STATES.
states=["assam","west bengal","arunachal pradesh","himachal pradesh","kerala","karnataka","gujarat"]
entstate=input('enter the name os state=')
if entstate in states:
    print("The state is present in the list")
else:
    print("The state is not present in the list")