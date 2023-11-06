import random

the_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def easy_mode():
    count_a = 10
    guess_a = True
    while guess_a:
        if count_a == 0:
            print("You've run out of guesses, you lose!")
            guess_a = False
        print(f"You have {count_a} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > the_number:
            print('''Too high.
Guess again.''')
        elif guess < the_number:
            print('''Too low.
Guess again.''')
        else:
            print(f"You got it! The answer was {the_number}")
            guess_a = False
        count_a -= 1

def hard_mode():
    count_b = 5
    guess_b = True
    while guess_b:
        if count_b == 0:
            print("You've run out of guesses, you lose!")
            guess_b = False
        print(f"You have {count_b} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > the_number:
            print('''Too high.
Guess again.''')
        elif guess < the_number:
            print('''Too low.
Guess again.''')
        else:
            print(f"You got it! The answer was {the_number}")
            guess_b = False
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