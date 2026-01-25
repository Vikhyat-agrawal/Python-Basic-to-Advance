with open('ch8 FILE I/O/donkey.txt','r') as f:
    content=f.read()
    content=content.replace('donkey','####')
with open('ch8 FILE I/O/donkey.txt','w') as f:
    f.write(content) 