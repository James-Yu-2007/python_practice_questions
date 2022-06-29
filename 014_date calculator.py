# input
year1 = int(input("year 1: "))
month1 = int(input("month 1: "))
day1 = int(input("day 1: "))
year2 = int(input("year 2: "))
month2 = int(input("month 2: "))
day2 = int(input("day 2: ")) 

# seeing if the input is valid
if year1 < year2:
    ok = True
elif year1 > year2:
    ok = False
elif year1 == year2:
    if month1 < month2:
        ok = True
    elif month1 > month2:
        ok = False
    elif month1 == month2:
        if day1 <= day2:
            ok = True
        elif day1 > day2:
            ok = False

if not ok:
    print("input invalid")
    exit

# seeing if the first inputed year is a leap year
def isLeapYear(year1):
    if year1 % 400 == 0:
        return True
    if year1 % 100 == 0:
        return False
    if year1 % 4 == 0:
        return True
    return False

# seeing how many days are in the first inputed month
def daysInMonth(year1, month1):

    if (month1 == 1) or (month1 == 3) or (month1 == 5) or (month1 == 7) or (month1 == 8) or (month1 == 10) or (month1 == 12):
        return 31
    else: 
        if (month1 == 2):
            if isLeapYear(year1):
                return 29
            else :
                return 28 

    return 30

# Calculate how many days are in the month before the month of the second inpput
if month2 != 1:
    month3 = int(month2 - 1)
else:
    month3 = 12

# seeing if the input is valid again
if month1 > 0 and month2 > 0 and day1 > 0 and day2 > 0 and month1 <= 12 and month2 <= 12 and day1 <= daysInMonth(year1, month1) and day2 <= daysInMonth(year2, month2):
    ok2 = True
else: 
    ok2 = False

if ok == False or ok2 == False:
    print("your input is invalid")
else:

# number of years
    if ok == True and ok2 == True:
        if year1 < year2:
            if month1 < month2:
                year = int(year2 - year1)
            elif month1 > month2:
                year = int(year2 - year1 - 1)
            elif month1 == month2:
                if day1 <= day2:
                    year = int(year2 - year1)
                elif day1 > day2:
                    year = int(year2 - year1 - 1)
        else:
            year = 0

# number or months
    if ok == True and ok2 == True:
        if month1 < month2:
            if day1 <= day2:
                month = int(month2 - month1)
            else:
                month = int(month2 - month1 - 1)
        elif month1 == month2:
            if day1 <= day2:
                month = 0
            else:
                month = 11
        else:
            if day1 <= day2:
                month = (12 - month1 + month2)
            else:
                month = (12 - month1 + month2 -1)

# number of days
    if ok == True and ok2 == True:
        if day1 == day2:
            day = 0
        elif day1 < day2:
            day = int(day2 - day1)
        else:
            day = int(daysInMonth(year2, month3) - day1 + day2)
    

# pluralization:
    if year != 1:
        pYear = "years"
    else:
        pYear = "year"

    if month != 1:
        pMonth = "months"
    else:
        pMonth = "month"

    if day != 1:
        pDay = "days"
    else:
        pDay = "day"



# final output

    if ok == False or ok2 == False:
        print("your input is invalid")
    else: 
        print("you are " + str(year) + " " + pYear + ", " + str(month) + " " + pMonth + " and " + str(day) + " " + pDay + " old")