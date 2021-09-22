#Lab 5

def isLeapYear(year):
    if not year % 4 == 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

print("Enter a date:")
date = input()
#MM/DD/YYYY
month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])

if month == 2:
    if 1 <= day <= 28:
        print("Valid date")
    elif day == 29:
        if isLeapYear(year):
            print("Valid date")
        else:
            print("invalid; not a leap year")
    else:
        print("invalid day")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if 1 <= day <= 30:
        print("Valid date")
    else:
        print("Day invalid")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if 1 <= day <= 31:
        print("valid date")
    else:
        print("day invalid")
else:
    print("Invalid date; month invalid")
