class sanket:
    sid:int
    stech:str
    
    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.stech=input("Enter Sanket's Tech.:")

class gopal:
    gid:int
    gtech:str
    
    def g_getdata(self):
        self.gid=input("Enter Gopal's ID:")
        self.gtech=input("Enter Gopal's Tech.:")
        
class mitesh:
    mid:int
    mtech:str
    
    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.mtech=input("Enter Mitesh's Tech.:")

class tops(sanket,gopal,mitesh):
    def printdata(self):
        print("-------Sanket's Data-------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Tech:",self.stech)
        print("-------Gopal's Data-------")
        print("Gopal's ID:",self.gid)
        print("Gopal's Tech:",self.gtech)
        print("-------Mitesh's Data-------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Tech:",self.mtech)

tp=tops()
tp.s_getdata()
tp.g_getdata()
tp.m_getdata()

tp.printdata()