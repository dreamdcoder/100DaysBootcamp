year = int(input("Which year you want to check? "))

Flag = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            Flag = True
        else:
            Flag = False
    else:
        Flag = True
else:
    Flag = False

if Flag:
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year")
