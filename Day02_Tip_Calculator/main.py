print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much percentage of tip would you like to give? like 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_amount = bill + tip_amount
bill_per_person = total_amount / people
final_bill = round(bill_per_person, 2)
print(f"Each person should pay: ${final_bill}")
