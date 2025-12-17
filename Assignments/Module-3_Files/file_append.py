id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

fl=open("test.txt",'a') #append mode
fl.write(f"\nID:{id}\nName:{name}\nCity:{city}")