# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.
import random
def snake_water_gun(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == 'snake' and computer_choice == 'water') or
            (user_choice == 'water' and computer_choice == 'gun') or   
            (user_choice == 'gun' and computer_choice == 'snake')):
        return "You win!"
    else:
        return "Computer wins!"
choices = ['snake', 'water', 'gun']
user_choice = input("Enter your choice (snake, water, gun): ").lower()
computer_choice = random.choice(choices)
result = snake_water_gun(user_choice, computer_choice)
print(f"Computer chose: {computer_choice}")
print(result)





'''use 
1=snake
0=water
-1=gun'''
def game(user, computer):
    if user == computer:
        return None
    if (user == 1 and computer == 0) or (user == 0 and computer == -1) or (user == -1 and computer == 1):
        return True
    else:
        return False
print("Welcome to Snake, Water, Gun game!")
user = int(input("Enter 1 for Snake, 0 for Water, -1 for Gun: "))
computer = random.randint(-1, 1)
result = game(user, computer)
print(f"Computer chose: {computer}")
if result == None:
    print("It's a tie!")
elif result:
    print("You win!")
else:
    print("Computer wins!") 