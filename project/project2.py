import random
n=random.randint(1,100)
guess= -1
while guess!=n:
    guess+=1
    a=int(input("Enter your guess: "))
    if a>n:
        print("Too high! Try again.")
    elif a<n:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {n} in {guess} attempts.")
        print("No of Guesses: ",guess )