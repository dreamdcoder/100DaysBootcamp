#year = int(input("Which year you want to check? "))

def isleapyear(year):
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
    return Flag

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    flag = isleapyear(year)
    if 1 <= month <=12:
        if flag and month == 2:
            return 29
        else:
            return  month_days[month-1]
    else:
        return "Invalid input for months"


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
