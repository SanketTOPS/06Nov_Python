fl=open('new.txt','w')

id=input("Enter an ID:")
name=input("Enter a Name:")

"""fl.write(id)
fl.write(name)"""

fl.write(f"ID={id}\nName={name}")