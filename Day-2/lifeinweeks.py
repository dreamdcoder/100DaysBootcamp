age = int(input("What is your current age? "))
span = 90

years = span - age
days = years * 365
weeks = years * 52
months = years * 12

message = f"You have {days} days, {weeks} weeks and {months} months left."
print(message)

