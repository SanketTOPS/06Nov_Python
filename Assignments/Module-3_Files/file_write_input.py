id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

fl=open("hello.txt",'w')
"""fl.write(id)
fl.write(name)
fl.write(city)"""

fl.write(f"\nID:{id}\nName:{name}\nCity:{city}")

fl.close()