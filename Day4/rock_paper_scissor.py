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

#Write your code below this line 👇
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
import random
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_input==0:
  print(rock)
elif user_input==1:
  print(paper)
else:
  print(scissors)
choices=[0, 1, 2]
computer_choice=random.choice(choices)
print("Computer Choice:")
if computer_choice==0:
  print(rock)
elif computer_choice==1:
  print(paper)
else:
  print(scissors) 

if user_input==0 and computer_choice==1:
  print("You lose")
elif user_input==0 and computer_choice==2:
  print("You win")
elif user_input==computer_choice:
  print("Its a draw")
elif user_input==1 and computer_choice==0:
  print("You win")
elif user_input==1 and computer_choice==2:
  print("You lose")
elif user_input==2 and computer_choice==0:
  print("You lose")
else:
  print("You win")
