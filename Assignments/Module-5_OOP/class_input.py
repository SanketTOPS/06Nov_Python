class student:
    id:int
    name:str
    
    def getdata(self):
        self.id=input("Enter an ID:")
        self.name=input("Enter a Name:")
    
    def printdata(self):
        print("ID:",self.id)
        print("Name:",self.name)
    
st=student()
st.getdata()
st.printdata()