print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15\nTip % : "))
people = int(input("How many people to split the bill?\nNumber of people :  "))

total = bill + bill * (tip / 100)
per_person = total / people
final_amount = (round(per_person,2))

print(f"Each person should pay ${final_amount}")