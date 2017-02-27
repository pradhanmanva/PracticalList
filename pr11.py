# WAP to check if the year is leap year.

year = 1800

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is leap year.")
        else:
            print(str(year) + " is not a leap year.")
    else:
        print(str(year) + " is leap year.")
else:
    print(str(year) + " is not a leap year.")
