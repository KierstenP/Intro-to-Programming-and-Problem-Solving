day = input("Enter the day the call started at: ")
timeStarted = int(input("Enter the time the call started at (hhmm): "))
callDuration = int(input("Enter the duration of the call (in minutes): "))
cost = 0
if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thu" or day == "Fri":
    if 800 <= timeStarted <= 1800:
        cost = float(callDuration * .4)
    elif timeStarted < 800 or timeStarted > 1800:
        cost = float(callDuration * .25)
elif day == "Sat" or day == "Sun":
    cost = float(callDuration * .15)
print("This call will cost $" + str(cost))
