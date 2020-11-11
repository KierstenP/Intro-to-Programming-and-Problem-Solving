def print_month_calender(num_of_days, starting_day):
    print("Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun", sep="\t")
    print("\t" * (starting_day-1), end='')
    i = 1
    for k in range(starting_day, (num_of_days+starting_day)):
        print(i, end="\t")
        i += 1
        if k % 7 == 0:
            print()
    if (((int(num_of_days) % 7) + int(starting_day)-1) % 7) == 0:
        return 0
    else:
        print()
        return ((int(num_of_days) % 7) + int(starting_day)-1) % 7

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False

def print_year_calender(year, starting_day):
    print()
    print("January", year)
    newStartPoint = print_month_calender(31, starting_day) +1

    print()
    print("February", year)
    if leap_year(year):
        leap = 29
        newStartPoint = ((print_month_calender(leap, newStartPoint)) + 1)
    else:
        leap = 28
        newStartPoint = ((print_month_calender(leap, newStartPoint))+1)
    print()
    print("March", year)
    newStartPoint = ((print_month_calender(31, newStartPoint)) + 1)
    print()
    print("April", year)
    newStartPoint = ((print_month_calender(30, newStartPoint)) + 1)
    print()
    print("May", year)
    newStartPoint = ((print_month_calender(31, newStartPoint)) + 1)
    print()
    print("June", year)
    newStartPoint = ((print_month_calender(30, newStartPoint)) + 1)
    print()
    print("July", year)
    newStartPoint = ((print_month_calender(31, newStartPoint)) + 1)
    print()
    print("August", year)
    newStartPoint = ((print_month_calender(31, newStartPoint)) + 1)
    print()
    print("September", year)
    newStartPoint = ((print_month_calender(30, newStartPoint)) + 1)
    print()
    print("October", year)
    newStartPoint = ((print_month_calender(31, newStartPoint)) + 1)
    print()
    print("November", year)
    newStartPoint = ((print_month_calender(30, newStartPoint)) + 1)
    print()
    print("December", year)
    print_month_calender(31, newStartPoint)

def main():
    year = int(input("Please input the year: "))
    starting_day = int(input("Please input the starting day: "))
    print_year_calender(year, starting_day)

main()
