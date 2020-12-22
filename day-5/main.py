import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator')


number_of_letter = int(
    input("How many letters would you like in your password? \n"))
number_of_symbol = int(input("How many symbols would you like? \n"))
number_of_numbers = int(input("How many numbers would you like? \n"))


password = ""

for num in range(0, number_of_letter):
    radom_number = random.randint(0, len(letters) - 1)
    password += letters[radom_number]

for num in range(0, number_of_symbol):
    radom_number = random.randint(0, len(symbols) - 1)
    password += symbols[radom_number]


for num in range(0, number_of_numbers):
    radom_number = random.randint(0, len(numbers) - 1)
    password += numbers[radom_number]

# print(password)

new_password = ""
for num in range(0, len(password)):
    random_num = random.randint(0, len(password) - 1)
    new_password += password[random_num]



print(new_password)
