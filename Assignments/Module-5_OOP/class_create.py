class student:
    id=12
    name='Sanket'
    
    def myfunc(self):
        print("This is user define function!")

#Object of class
st=student()
print("ID:",st.id)
print("Name:",st.name)

st.myfunc()