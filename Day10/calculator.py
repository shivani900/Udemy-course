import art
# Add
def add(n1,n2):
  return n1+n2

# Subtract
def subtract(n1,n2):
  return n1-n2

#MULTIPLY
def multiply(n1, n2):
  return n1*n2

# Divide
def divide(n1,n2):
  return n1/n2

operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(art.logo)
  num1=float(input("Enter your first number: "))
  for i in operations:
    print(i)
  should_continue = True
  while should_continue:
    operation = input("Pick an operation: ")
    num2=float(input("Enter your second number: "))
    function=operations[operation]
    answer=function(num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
    choice = input(f"Type y to continue with {answer} or type n to start a new calcultion: ")
    if choice=="y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
    