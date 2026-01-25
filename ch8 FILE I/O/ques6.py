with open('ch8 FILE I/O/python.txt','r') as f:
    content=f.read()
    if 'python' in content.lower():
        print("The word 'python' is present in the file.")
    else:
        print("The word 'python' is not present in the file.")