# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random
def game():
    score = random.randint(0, 100)  # Simulating a game score
    print(f"Your score is: {score}")
    return score

# Read the previous Hi-score from the file
with open('ch8 FILE I/O/Hi-score.txt', 'r') as f:
    hi_score = f.read()
    hi_score = int(hi_score) if hi_score else 0 

# Play the game and get the current score
current_score = game()  

# Update the Hi-score if the current score is higher
if current_score > hi_score:
    print("Congratulations! You've beaten the Hi-score!")
    with open('ch8 FILE I/O/Hi-score.txt', 'w') as f:
        f.write(str(current_score))
else:
    print("You did not beat the Hi-score. Better luck next time!")