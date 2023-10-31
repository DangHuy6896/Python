from art_day11 import logo
from sys import exit
import random
import os

cards = [
  ["A", 11],
  ["2", 2],
  ["3", 3],
  ["4", 4],
  ["5", 5],
  ["6", 6],
  ["7", 7],
  ["8", 8],
  ["9", 9],
  ["10", 10],
  ["J", 10],
  ["Q", 10],
  ["K", 10],
]

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def another_change():
  global your_cards, computer_cards, your_cards_value, computer_cards_value, container_cards_player, container_cards_comp, container_final_player, container_final_comp
  continue_play = True
  count = 1
  while continue_play:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another_card == 'y':
      count += 1
      your_cards.append(random.choice(cards))
      container_cards_player.append(your_cards[count][0])
      your_cards_value += your_cards[count][1]
      container_final_player = ', '.join(container_cards_player)
      if computer_cards_value < 17:
        computer_cards.append(random.choice(cards))
        container_cards_comp.append(computer_cards[count][0])
        computer_cards_value += computer_cards[count][1]
        container_final_comp = ', '.join(container_cards_comp)
        if computer_cards[0][0] == "A" and computer_cards[1][0] == "A":
          if computer_cards[count][0] == "A":
            computer_cards_value -= 10
            computer_cards[count][1] = 1
          elif computer_cards[count][0] != "A":
            if computer_cards_value > 21 and computer_cards[1][1] == 11:
              computer_cards_value -= 10 
              computer_cards[1][1] = 1
        elif computer_cards[0][0] == "A" and computer_cards[1][0] != "A":
          if computer_cards[count][0] == "A":
            computer_cards_value -= 10
            computer_cards[count][1] = 1
          elif computer_cards[count][0] != "A":
            if computer_cards_value > 21 and computer_cards[0][1] == 11:
              computer_cards_value -= 10
              computer_cards[0][1] = 1
        elif computer_cards[0][0] != "A" and computer_cards[1][0] == "A":
          if computer_cards[count][0] == "A":
            computer_cards_value -= 10
            computer_cards[count][1] = 1
          elif computer_cards[count][0] != "A":
            if computer_cards_value > 21 and computer_cards[1][1] == 11:
              computer_cards_value -= 10
              computer_cards[1][1] = 1
        elif computer_cards[0][0] != "A" and computer_cards[1][0] != "A":
          if computer_cards[count][0] == "A":
            if computer_cards_value > 21:
              computer_cards_value -= 10
              computer_cards[count][1] = 1
          elif computer_cards[count][0] != "A":
            if computer_cards_value > 21:
              met_qua_3 = 0
              for thc in range(len(computer_cards) - 1):
                if computer_cards[thc][0] =="A" and computer_cards[thc][1] == 11:
                  met_qua_3 += 1
                  computer_cards_value -= 10
                  computer_cards[thc][1] = 1
      if your_cards[0][0] == "A" and your_cards[1][0] == "A":
        if your_cards[0][1] == 1 and your_cards[1][1] == 11:
          if your_cards[count][0] == "A":
            your_cards_value -= 10
            your_cards[count][1] = 1
            if your_cards_value > 21:
              your_cards_value -= 10
              your_cards[1][1] = 1
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
            else:              
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
          elif your_cards[count][0] != "A" and your_cards_value > 21:
            your_cards_value -= 10
            your_cards[1][1] = 1
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
          elif your_cards[count][0] != "A" and your_cards_value <= 21:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
        elif your_cards[0][1] == 1 and your_cards[1][1] == 1:
          if your_cards[count][0] == "A":
            your_cards_value -= 10
            your_cards[count][1] = 1
            if your_cards_value > 21:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
            else:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
          elif your_cards[count][0] != "A":
            if your_cards_value > 21:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
            else:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
      elif your_cards[0][0] == "A" and your_cards[1][0] != "A":
        if your_cards[count][0] == "A":
          your_cards_value -= 10 
          your_cards[count][1] = 1
          if your_cards_value > 21:
            if your_cards[0][1] == 11:
              your_cards_value -= 10
              your_cards[0][1] = 1
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
            elif your_cards[0][1] == 1:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
          else:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
        elif your_cards[count][0] != "A":
          if your_cards_value > 21:
            if your_cards[0][1] == 11:
              your_cards_value -= 10 
              your_cards[0][1] = 1
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
            elif your_cards[0][1] == 1:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
          else:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
      elif your_cards[0][0] != "A" and your_cards[1][0] == "A":
        if your_cards[count][0] == "A":
          your_cards_value -= 10 
          your_cards[count][1] = 1
          if your_cards_value > 21:
            if your_cards[1][1] == 11:
              your_cards_value -= 10
              your_cards[1][1] = 1
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
            elif your_cards[1][1] == 1:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
          else:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
        elif your_cards[count][0] != "A":
          if your_cards_value > 21:
            if your_cards[1][1] == 11:
              your_cards_value -= 10 
              your_cards[1][1] = 1
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
            elif your_cards[1][1] == 1:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
          else:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
      elif your_cards[0][0] != "A" and your_cards[1][0] != "A":
        if your_cards[count][0] == "A":
          if your_cards_value > 21:
            your_cards_value -= 10 
            your_cards[count][1] = 1
            if your_cards_value > 21:
              met_qua_1 = 0
              for tha in range(len(your_cards) - 1):
                if your_cards[tha][0] == "A" and your_cards[tha][1] == 11:
                  met_qua_1 += 1
                  your_cards_value -= 10
                  your_cards[tha][1] = 1
              if met_qua_1 == 0:
                print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
                print(f"Computer's first card: {computer_cards[0][0]}")
                print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
                print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
                if your_cards_value > 21 and computer_cards_value > 21:
                  print("Draw")
                else:
                  print("You lose!")
                continue_play = False
            else:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
          else:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
        if your_cards[count][0] != "A":
          if your_cards_value > 21:
            met_qua_2 = 0
            for thb in range(len(your_cards) - 1):
              if your_cards[thb][0] == "A" and your_cards[thb][1] == 11:
                met_qua_2 += 1
                your_cards_value -= 10
                your_cards[thb][1] = 1
            if met_qua_2 == 0:
              print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
              print(f"Computer's first card: {computer_cards[0][0]}")
              print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
              print(f"Computer's final hand: [{container_final_comp}], final score: {computer_cards_value}")
              if your_cards_value > 21 and computer_cards_value > 21:
                print("Draw")
              else:
                print("You lose!")
              continue_play = False
          else:
            print(f"Your cards: [{container_final_player}], current score: {your_cards_value}")
            print(f"Computer's first card: {computer_cards[0][0]}")
    elif another_card == 'n':
      print(f"Your final hand: [{container_final_player}], final score: {your_cards_value}")
      print(f"Computer's final hand: [{container_final_comp}] final score: {computer_cards_value}")
      if your_cards_value < 22 and computer_cards_value < 22:
        if your_cards_value > computer_cards_value:
          print("You win")
        elif your_cards_value < computer_cards_value:
          print("You lose")
        else:
          print("Draw")
      elif your_cards_value < 22 and computer_cards_value > 21:
        print("You win")
      elif your_cards_value > 21 and computer_cards_value < 22:
        print("You lose")
      elif your_cards_value > 21 and computer_cards_value > 21:
        print("Draw")
      continue_play = False
    else:
      another_change()
  wanna_play()

def wanna_play():
  global your_cards, computer_cards, your_cards_value, computer_cards_value, container_cards_player, container_cards_comp, container_final_player, container_final_comp
  your_cards = []
  computer_cards = []
  your_cards_value = 0
  computer_cards_value = 0
  container_cards_player = []
  container_cards_comp = []
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if play == 'y':
    clear_console()
    print(logo)
    for n in range(2):
      choice_card = random.choice(cards)
      your_cards.append(choice_card)
      container_cards_player.append(your_cards[n][0])
      choice_card = random.choice(cards)
      computer_cards.append(choice_card)
      container_cards_comp.append(computer_cards[n][0])
    container_final_player = ', '.join(container_cards_player)
    container_final_comp = ', '.join(container_cards_comp)
    if your_cards[0][0] == "A" and your_cards[1][0] == "A":
      your_cards[0][1] = 1
      your_cards_value = your_cards[0][1] + your_cards[1][1]
      print(f"Your card: [{your_cards[0][0]}, {your_cards[1][0]}], highest score: {your_cards_value}")
    else:
      your_cards_value = your_cards[0][1] + your_cards[1][1]
      print(f"Your card: [{your_cards[0][0]}, {your_cards[1][0]}], current score: {your_cards_value}")
    if computer_cards[0][0] == "A" and computer_cards[1][0] == "A":
      computer_cards[0][1] = 1
      computer_cards_value = computer_cards[0][1] + computer_cards[1][1]
      print(f"Computer's first card: {computer_cards[0][0]}")
    else:
      computer_cards_value = computer_cards[0][1] + computer_cards[1][1]
      print(f"Computer's first card: {computer_cards[0][0]}")
    another_change()    
  elif play == 'n':
    clear_console()
    print("Goodbye babe!")
    exit()
  else:
    wanna_play()
  
wanna_play()