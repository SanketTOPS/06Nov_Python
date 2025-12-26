class Father:
    car:int
    bal:int
    
    def getdata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter bank balance details:")

class Son(Father):
    def printdata(self):
        print("Car:",self.car)
        print("Balance:",self.bal)

sn=Son()
sn.getdata()
sn.printdata()