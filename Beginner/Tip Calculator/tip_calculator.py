# 1. Create a greeting for your program.
print("Welcome to the tip calculator")
# 2.
bill = float(input("What was the total bill? \n $"))
# 3.
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
percentage_tip = tip/100
total_tip_amount = bill * percentage_tip
# 4.
total_bill = bill + total_tip_amount
# 5.
people = int(input("How many people to split the bill? \n"))
bill_for_person = round((total_bill/people),2)
final_amount = "{:.2f}".format(bill_for_person)
print(f"Each person should pay: ${final_amount}")