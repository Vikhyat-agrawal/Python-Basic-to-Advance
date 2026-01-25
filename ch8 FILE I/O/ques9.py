with open('ch8 FILE I/O/text.txt','r') as f:
    content = f.read()
    
with open('ch8 FILE I/O/this.txt','r') as f:
    contentnew = f.read()

if content == contentnew:
    print("The two files have identical content.")
else:
    print("The two files do not have identical content.")