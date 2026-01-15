d={}
for i in range(3):
    name=input("Enter your name: ")
    lang=input("Enter your favorite language: ")

    d.update({name:lang})
print(d)