import random
from art import logo

def intro():
    print(logo)
    print("Welcome to the number Guessing game!")
    print("I'm thinking of a number between 1 and 100")
    
    
intro()

random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == 'easy':
    lives = 10
else:
    lives = 5
    
    
print(f"You have {lives} attempts remaining to guess the number.")



is_found = False

while is_found == False and lives != 0:
    guess = int(input("Make a guess "))
    if guess > random_number:
        print("Too high.\nGuess again")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    elif guess < random_number:
        print("Too low.\nGuess agin")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was: {random_number}")
        is_found = True
    
if lives == 0: 
    print("You've run out of guesses, you lose.")

