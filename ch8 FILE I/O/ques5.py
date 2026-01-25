list=["donkey","monkey","elephant","tiger","lion"]
with open('ch8 FILE I/O/animal.txt','r') as f:
    content=f.read()
    for word in list:
        content=content.replace(word,'####')
with open('ch8 FILE I/O/animal.txt','w') as f:
    f.write(content) 