import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]


user_number = int(input("Please select a value: 0 Rock, 1 Paper, 2 Scissors "))
computer_number = random.randint(0, len(game_images) - 1)

user_choice = game_images[user_number]
computer_choice = game_images[computer_number]


message = ""

if(user_number >= 3 and user_number < 0):
    print('Vous avez entré un nombre invalide')
else:
    if user_number == 0:
        if computer_number == 0:
            message = 'Egalité'
        elif computer_number == 1:
            message = "l'ordinateur a gagné"
        elif computer_number == 2:
            message = "Vous avez gagné"
    elif user_number == 1:
        if computer_number == 0:
            message = 'Vouas avez gagné'
        elif computer_number == 1:
            message = "Egalité"
        elif computer_number == 2:
            message = "Vous avez perdu"
    else:
        if computer_number == 0:
            message = 'Vous avez perdu'
        elif computer_number == 1:
            message = "Vous avez perdu"
        elif computer_number == 2:
            message = "égalité"


print(user_choice)
print(computer_choice)
print(message)

