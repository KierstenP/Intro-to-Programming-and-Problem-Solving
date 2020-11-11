n = int(input("Please input a positive integer: "))
evenDigitCounter = 0
oddDigitCounter = 0
digit = 0
number = 0
for i in range(1, (n+1), 1):
    number = i
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            evenDigitCounter += 1
        else:
            oddDigitCounter += 1
        number = (number // 10)
    if evenDigitCounter > oddDigitCounter:
        print(i)
    evenDigitCounter = 0
    oddDigitCounter = 0
