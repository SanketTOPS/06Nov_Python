import re

mystr="That is Python!7477582"

#x=re.findall("\w",mystr)
#x=re.findall("\W",mystr)
#x=re.findall("\s",mystr)
#x=re.findall("\S",mystr)
#x=re.findall("\d",mystr)
#x=re.findall("\D",mystr)
#x=re.findall("\AThis",mystr)
x=re.findall("88\Z",mystr)
print(x)