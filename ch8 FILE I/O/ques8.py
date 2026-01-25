with open('ch8 FILE I/O/text.txt','r') as f:
    content=f.read()
with open('ch8 FILE I/O/this.txt','w') as f1:
    f1.write(content)