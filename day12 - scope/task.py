import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)

if difficulty == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess > number:
        print("Too high.")
        lives -= 1
    else:
        print("Too low.")
        lives -= 1
        
        
if lives == 0:
    print("You've run out of guesses, you lose.")