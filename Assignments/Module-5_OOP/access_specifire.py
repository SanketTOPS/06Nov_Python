class Students:
    #private
    __stid=12
    __stnm="Sanket"
    
    def __getdata(self): #private
        print("This is getdata!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
        
    def printdata(self):
        self.__getdata()

st=Students()
#st.getdata()

st.printdata()


    