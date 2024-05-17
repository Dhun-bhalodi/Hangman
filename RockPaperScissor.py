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
game_choice = [rock,paper,scissors]
user_choice= int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissor-"))
if user_choice>=3 or user_choice<0:
    print("You typed an invalid number, you lose!\n")
else:
    print(game_choice[user_choice])

computer_choose = random.randint(0,2)
print("Computer chose:")
print(game_choice[computer_choose])

if user_choice==computer_choose:
    print("It's a draw")
elif user_choice==0:
    if computer_choose==1:
         print("You loose")
    elif computer_choose==2:
         print("You won")
elif user_choice==1:
    if computer_choose==0:
         print("You loose")
    elif computer_choose==2:
         print("You won")
elif user_choice==2:
    if computer_choose==0:
         print("You loose")
    elif computer_choose==1:
         print("You win")

