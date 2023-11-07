import random

the_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def easy_mode():
    count_a = 5
    while count_a != -1:
        if count_a == 0:
            print("You've run out of guesses, you lose!")
        else:
            print(f"You have {count_a} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > the_number:
                print("Too high.\nGuess again.")
            elif guess < the_number:
                print("Too low.\nGuess again.")
            else:
                print(f"You got it! The answer was {the_number}")
                count_a = 0
        count_a -= 1

def hard_mode():
    count_b = 5
    while count_b != -1:
        if count_b == 0:
            print("You've run out of guesses, you lose!")
        else:
            print(f"You have {count_b} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > the_number:
                print("Too high.\nGuess again.")
            elif guess < the_number:
                print("Too low.\nGuess again.")
            else:
                print(f"You got it! The answer was {the_number}")
                count_b = 0
        count_b -= 1

def difficult_level():
    choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_level == "easy":
        easy_mode()
    elif choose_level == "hard":
        hard_mode()
    else:
        difficult_level()

difficult_level()