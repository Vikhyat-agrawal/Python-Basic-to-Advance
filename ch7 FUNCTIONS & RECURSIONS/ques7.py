def multi(n):
    print(f"The multiplication table of {n} is:")
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")
num = int(input("Enter a number: "))
multi(num)