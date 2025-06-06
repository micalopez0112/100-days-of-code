import random

#import hangman_words


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

blanks = ''
for letter in chosen_word:
    blanks += "_"
print(blanks)

game_over = False
correct_guesses = []
lives = 6

while not game_over:
    display = ''    
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_guesses:
        print(f"You've already guessed {guess}")
        
    for letter in chosen_word:
        if letter == guess:
            correct_guesses.append(letter)
            display += letter
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_" 
            
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
    print(display)
    
    if "_" not in display:
        print("You win.") 
        game_over = True
        
    if lives == 0:
        print("You lose.")
        game_over = True