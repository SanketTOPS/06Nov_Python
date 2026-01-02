import re

mystr="This is Python!"

#x=re.search("This",mystr)
#x=re.search("Python",mystr)
x=re.search("This",mystr)
print(x)

if x:
    print("Match done!")
else:
    print("Error!")

