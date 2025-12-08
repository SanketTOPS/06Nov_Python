a=54
print("A:",a)

def getA():
    global a
    a+=10
    print("A:",a)

getA()