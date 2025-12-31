fl=open('new.txt','a')

id=input("Enter an ID:")
name=input("Enter a Name:")


fl.write(f"\nID={id}\nName={name}")