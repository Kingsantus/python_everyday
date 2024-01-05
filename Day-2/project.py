print("Welcome to the tip calculator")
bill = input("What was the total bill?  $")
bill = float(bill)
percent = input("What percentage tip would you like to give? ")
percent = float(percent)
percent = percent/100
tip = percent * bill
total_bill = tip + bill
people = input("How many people to split the bill? ")
people = int(people)
per_bill = round(total_bill/people, 2)
print(f"Each person should pay: ${per_bill}")