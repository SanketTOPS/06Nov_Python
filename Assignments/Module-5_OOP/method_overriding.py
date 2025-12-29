class Student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class home(Student):
    def getdata(self, id, name):
        return super().getdata(id, name)

class about(Student):
    def getdata(self, id, name):
        return super().getdata(id, name)
