print("Enter number in the simplified Roman system: ")
romanNum = input()
countM = 0
countD = 0
countC = 0
countL = 0
countX = 0
countV = 0
countI = 0
previousValue = 1001
currentValue = 0
decimalValue = 0
check = True
for i in romanNum:
    if i == "M":
        decimalValue += 1000
        currentValue = 1000
        countM += 1
    elif i == "D":
        decimalValue += 500
        currentValue = 500
        countD += 1
    elif i == "C":
        decimalValue += 100
        currentValue = 100
        countC += 1
    elif i == "L":
        decimalValue += 50
        currentValue = 50
        countL += 1
    elif i == "X":
        decimalValue += 10
        currentValue = 10
        countX += 1
    elif i == "V":
        decimalValue += 5
        currentValue = 5
        countV += 1
    elif i == "I":
        decimalValue += 1
        currentValue = 1
        countI += 1
    if currentValue > previousValue or countD > 1 or countL > 1 or countV > 1\
            or countC > 4 or countX > 4 or countI > 4:
        print()
        print(romanNum, "is not a legal number in the simplified Roman numeral system.")
        check = False
        break
    else:
        previousValue = currentValue
if check == True:
    print()
    print(romanNum, "is", decimalValue)
