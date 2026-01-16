n=int(input("Enter a number: "))
fact=1
for i in range(n+1):
    if i>0:
        fact=fact*i
print(f"The factorial of {n} is {fact}")
    