from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
dict = {}
continue_biding = True
while continue_biding:
  name = input("Enter your name: ")
  bid = int(input("Enter the bid amount: $"))
  dict[name] = bid
  choice = input("Are there any other bidders Type 'yes' or 'no' ")
  if choice == "no":
    continue_biding = False
    max_bid = 0
    winner = ""
    for key in dict:
      if dict[key] > max_bid:
        max_bid = dict[key]
        winner = key
    print(f"The winner is {winner} with bid of ${max_bid}")
  else:
    clear()
  
    
