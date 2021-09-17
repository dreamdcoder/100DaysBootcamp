print("Welcome to the tip calculator!")
bill = float(input("Whats was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10,12 or ,15? "))
num_ppl = int(input("How many people to split the bill? "))

total_bill = bill + bill * (tip_percent/100)

bill_per_person = round(total_bill/num_ppl, 2)



# print(f"Your final bill is ${final_bill} : \nbill ${bill} + tip ${tip_amount}")
print(f"Each person should pay: ${bill_per_person:.2f}")
