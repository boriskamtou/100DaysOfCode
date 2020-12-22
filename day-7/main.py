import random
import art
import words


print(art.logo)

display = []



lives = 6

random_number = random.randint(0, len(words.word_list) - 1)
random_word = words.word_list[random_number]

letters_not_in = []

for letter in random_word:
    display.append("_")


while lives > 0 and "_" in display:
    guess = input("Guest a letter ").lower()
    for i in range(0, len(random_word)):
        if random_word[i] == guess:
            display[i] = guess
            

    if guess not in random_word:
        lives -= 1
        print(art.stages[lives])
        
        if guess not in letters_not_in:
            letters_not_in.append(guess)
            print(f"{guess} it's not in the word.")
        else:
            print(f"{guess} has already been used but it is not a good letter.")
      
    if guess in display:
        print(f"You already guessed {guess}.")     
    

    print(f"{' '.join(display)}")


if "_" not in display:
    print("\n")
    print("You win")
elif lives == 0:
    print("\n")
    print("You Lose")
else:
    print("\n")
    print("You lose")
