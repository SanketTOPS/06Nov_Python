import re

mystr="This is Python!5489897846"

#x=re.findall('^Python',mystr)
#x=re.findall("^[A-Z]",mystr)
x=re.findall('48$',mystr)
print(x)