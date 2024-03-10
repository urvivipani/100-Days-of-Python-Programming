#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
final_bill = float(input("What was the total bill?\n$"))
tip = float(input("What percentage of tip would you like to give? 10, 12, or 15?\n"))

no_of_people = int(input("How many people to split the bill?\n"))

tip_amount = (final_bill/no_of_people) * (tip/100)
final_amount = round(final_bill/no_of_people + tip_amount , 2)
#Format the result to 2 decimal places = 33.60
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay ${final_amount}.")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
