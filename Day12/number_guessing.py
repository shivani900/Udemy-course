import art
import random

def set_difficulty():
  level=input("Which level you choose hard or easy: ")
  if level=="hard":
    return 5
  elif level=="easy":
    return 10

def check_answer(guess , answer, turns):
  if guess>answer:
    print("too high")
    return turns-1
  elif guess<answer:
    print("too low")
    return turns-1
  else:
    print(f"you got this ,answer is {answer}")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer=random.randint(1,100)
turns=set_difficulty()
guess = 0
while guess!=answer:
  print(f"You have {turns} turns left.")
  guess=int(input("Take a guess! "))
  turns = check_answer(guess,answer,turns)
  if turns == 0:
    print("You lost")
    break
  elif guess != answer:
    print("Guess again")
  
  
  


    