import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


your_choose = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
options = [rock, paper, scissors]
your_choose_material = options[your_choose]
print(f"{your_choose_material}\n")
computer_choose = random.randint(0, 2)
computer_choose_material = options[computer_choose]
print("Computer chose:\n")

if your_choose == computer_choose:
  print(f"{computer_choose_material}\nDraw")
elif (your_choose == 0 and computer_choose == 2) or (your_choose == 1 and computer_choose == 0) or (your_choose == 2 and computer_choose == 1):
  print(f"{computer_choose_material}\nYou win")
else:
  print(f"{computer_choose_material}\nYou lose")