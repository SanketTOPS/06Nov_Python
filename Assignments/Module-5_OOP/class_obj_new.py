class Student:
    stid:int
    stnm:str
    
    def getdata(self):
        self.stid=input("Enter an ID:")
        self.stnm=input("Enter a Name:")
    
    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

st=Student()
st.getdata()
st.printdata()
        