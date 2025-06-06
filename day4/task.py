import random
# import my_module

# random_integer = random.randint(1, 100)
# print(random_integer)

# print(my_module.my_favourite_number)

# random_number = random.random()
# print(random_number)

# random_float = random.uniform(1, 10)
# print(random_float)

# if random_number > 0.5:
#     print("Heads")
# else:
#     print("Tails")

options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")

if computer_choice == user_choice:
    print(f"Both players selected {user_choice}. It's a draw!")
elif computer_choice == "Rock" and user_choice == "Scissors":
    print("Rock beats Scissors. You lose!")
elif computer_choice == "Scissors" and user_choice == "Paper":
    print("Scissors beats Paper. You lose!")
elif computer_choice == "Paper" and user_choice == "Rock":
    print("Paper beats Rock. You lose!")
else:
    print("You win!")