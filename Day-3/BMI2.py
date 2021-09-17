weight = float(input("Please Enter Your weight in kg: "))
height = float(input("please enter your height in meters: "))

BMI = round(weight / (height ** 2))
print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print(f"You are underweight.")
elif BMI < 25:
    print(f"You have normal weight.")
elif BMI < 30:
    print(f"You are overweight.")
elif BMI < 35:
    print(f"You are obese.")
else:
    print(f"You are clinically obese")

ideal_weight = 25 * (height ** 2)
print(f"Your ideal weight in kg is: {ideal_weight}")
