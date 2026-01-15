d={"hello":"namaste","hi":"namaskar","bye":"alvida"}
word=input("Enter the word: ")
print("The meaning of",word,"is",d.get(word,"Not found in dictionary"))