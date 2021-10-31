weight = float(input("Please Enter Your weight in kg: "))
height = float(input("please enter your height in meters: "))

BMI = weight/height**2
print(f"your BMI is {BMI}")
ideal_weight = 25*(height**2)
print(f"your ideal weight in kg is: {ideal_weight}")
