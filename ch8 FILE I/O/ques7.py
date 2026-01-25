with open('ch8 FILE I/O/python.txt','r') as f:
    i=1
    content=f.read()
    for line in content.split('\n'):
        if 'python' in line.lower():
            print(f"The word 'python' is present in line {i}.")
        i+=1
    