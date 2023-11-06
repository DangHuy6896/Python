import os
from art_day9 import logo

print(logo)

info_players = []
any_other = True

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def info_player(x, y):
  player = {}
  player["name"] = x
  player["bid"] = y
  info_players.append(player)

def high_bid():
  max_name = ""
  max_bid = 0
  for check in range(len(info_players)):
    if info_players[check]["bid"] > max_bid:
      max_name = info_players[check]["name"]
      max_bid = info_players[check]["bid"]
  print(f"The winner is {max_name} with a bid of ${max_bid}.")

def another_turn():
  global any_other
  any_one_else = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if any_one_else == 'yes':
    any_other = True
    clear_console()
  elif any_one_else == 'no':
    any_other = False
    clear_console()
    high_bid()
  else:
    print("Please type the correct diaper.")
    another_turn()

while any_other:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  info_player(name, bid)
  another_turn(any_other)