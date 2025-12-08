"""def getsum(a,b):
    return a+b"""

"""x=getsum(34,65)
print(x)"""


def getvalue(a,b):
    return a,b

def sum():
    x=getvalue(34,56)
    print("Sum:",x[0]+x[1])
    
def sub():
    x=getvalue(34,56)
    print("Sub:",x[0]-x[1])
    
def mul():
    x=getvalue(34,56)
    print("Mul:",x[0]*x[1])



sum()
sub()
mul()