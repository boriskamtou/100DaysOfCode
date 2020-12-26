from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

print("Welcome to the secret auction program.")


list_user = []
user = {}

is_end = False


def create_user(name, bid):
  user = {}
  user["name"] = name
  user["bid"] = bid
  list_user.append(user)

while is_end == False:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))

  create_user(name, bid)

  result = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if result == 'no':
    max_bid = 0
    win_name = ""
    for i in range(len(list_user)):

      user_dictionny = list_user[i]
      winner_bid = user_dictionny["bid"]
      winner_name = user_dictionny["name"]

      if winner_bid > max_bid:
        max_bid = winner_bid
        win_name = winner_name

    clear()
    is_end = True
  else:
    clear()

  
print(f"The winner is {win_name} with a bid of {max_bid}")
