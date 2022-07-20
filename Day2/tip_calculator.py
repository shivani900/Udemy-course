
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill=int(input("enter your bill? $"))
no_of_people=int(input("total number of people? "))
tip=int(input("Enter the amount of tip 10,12 or 15?"))
tip_amount=(bill*tip)/100
total_amount=bill+tip_amount
bill_each_person=round(total_amount/no_of_people,2)
print(f"Each person has to pay {bill_each_person}")