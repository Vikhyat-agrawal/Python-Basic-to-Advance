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
