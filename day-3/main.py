# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


lower_name1 = name1.lower()
lower_name2 = name2.lower()


str_true = "true"
str_love = "love"


num_letter_true_in_names = 0
num_letter_love_in_names = 0

# true in name1
for letter in str_true:
    if letter == "t":
        num_t = lower_name1.count(letter)
        num_letter_true_in_names += num_t
    elif letter == "r":
        num_r = lower_name1.count(letter)
        num_letter_true_in_names += num_r
    elif letter == "u":
        num_u = lower_name1.count(letter)
        num_letter_true_in_names += num_u
    else:
        num_e = lower_name1.count(letter)
        num_letter_true_in_names += num_e


# true in name1
for letter in str_true:
    if letter == "t":
        num_t = lower_name2.count(letter)
        num_letter_true_in_names += num_t
    elif letter == "r":
        num_r = lower_name2.count(letter)
        num_letter_true_in_names += num_r
    elif letter == "u":
        num_u = lower_name2.count(letter)
        num_letter_true_in_names += num_u
    else:
        num_e = lower_name2.count(letter)
        num_letter_true_in_names += num_e

# Love in name1
for letter in str_love:
    if letter == "l":
        num_t = lower_name1.count(letter)
        num_letter_love_in_names += num_t
    elif letter == "o":
        num_r = lower_name1.count(letter)
        num_letter_love_in_names += num_r
    elif letter == "v":
        num_u = lower_name1.count(letter)
        num_letter_love_in_names += num_u
    else:
        num_e = lower_name1.count(letter)
        num_letter_love_in_names += num_e

# Love in name2
for letter in str_love:
    if letter == "l":
        num_t = lower_name2.count(letter)
        num_letter_love_in_names += num_t
    elif letter == "o":
        num_r = lower_name2.count(letter)
        num_letter_love_in_names += num_r
    elif letter == "v":
        num_u = lower_name2.count(letter)
        num_letter_love_in_names += num_u
    else:
        num_e = lower_name2.count(letter)
        num_letter_love_in_names += num_e


score_in_str = str(num_letter_true_in_names) + str(num_letter_love_in_names)

score_in_int = int(score_in_str)


if score_in_int < 10 or score_in_int > 90:
    print(
        f"Your score is {score_in_int}, you go together like coke and mentos.")

elif score_in_int >= 40 and score_in_int <= 50:
    print(f"Your score is {score_in_int}, you are alright together.")

else:
    print(f"Your score is {score_in_int}")
