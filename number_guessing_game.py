# 1. number range 1-10 
# 2. set our number = 4
# while loop(to keep asking guesses)
# 3.ask the user to guess
# 4. check if the user's input equal to chosen number
# 4a. if user's guess is correct
#       => print congratulation 
#       =>end
# 4b. if user guess is wrong 
##      option1: user's guess is higher than chosen number=> 
#           =>hint=lower, 
#           =>ask user to enter a new number
##      option2: user's guess is lower than chosen number =>
#           =>hint=higher,
#           =>ask user to enter a new number


import random

def number_guessing_game():
    random_number = random.randint(1, 10)
    guess = None
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    while guess != random_number:
        guess = int(input("Take a guess: "))
        
        if guess < random_number:
            print("Higher!")
        elif guess > random_number:
            print("Lower!")
        else:
            print("Congratulations! You've guessed the right number.")

if __name__ == "__main__":
    number_guessing_game()
