print("Welcome to the calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 12, 13, 15? "))
people = int(input("How many people have to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
final_amount = round(bill_with_tip / people, 2)

print(f"Each person should pay: ${final_amount}")
