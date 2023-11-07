from art_day14 import logo, vs
from data_day14 import data
from random import randint
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick():
    return data[randint(0, 49)]

def choice():
    count = 0
    score = 0
    k_g = True
    while k_g:
        count += 1         
        slot_A = pick()
        slot_B = pick()
        while slot_A['name'] == slot_B['name']:
            slot_A = pick()
            slot_B = pick()
        clear_console()
        print(logo)
        if count > 1:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {slot_A['name']}, a {slot_A['description']}, from {slot_A['country']}.")
        print(vs)
        print(f"Against B: {slot_B['name']}, a {slot_B['description']}, from {slot_B['country']}.")
        who = input("Who has more followers? Type 'A' or 'B': ").upper()  
        if who == 'A':
            if slot_A['follower_count'] >= slot_B['follower_count']:
                score += 1
            else:
                clear_console()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                k_g = False
        elif who == 'B':
            if slot_B['follower_count'] >= slot_A['follower_count']:
                score += 1
            else:
                clear_console()
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}") 
                k_g = False    
        else:
            choice()

choice()

    