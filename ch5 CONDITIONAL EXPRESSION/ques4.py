name=input("Enter your name: ")
a=len(name)
if a<10:
    print("Your name is short")
elif a==10:
    print("Your name is of normal length")
else:
    print("Your name is long")