print("Please enter lengths of a triangle's sides")
firstSide = int(input("Length of the first side: "))
secondSide = int(input("Length of the second side: "))
thirdSide = int(input("Length of the third side: "))
marginOfError = 0.001
if firstSide == secondSide and secondSide == thirdSide:
    print(firstSide, secondSide, thirdSide, "form and equilateral triangle.")
elif firstSide == secondSide or secondSide == thirdSide or thirdSide == firstSide:
    if (thirdSide - marginOfError) <= (((firstSide ** 2) + (secondSide ** 2)) ** 1/2) <= (thirdSide + marginOfError):
        print(str(firstSide) + "," + str(secondSide) + "," + str(thirdSide), "form an isosceles right triangle")
    elif (secondSide - marginOfError) <= (((firstSide ** 2) + (thirdSide ** 2) ** 1/2)) <= (secondSide + marginOfError):
        print(str(firstSide) + "," + str(secondSide) + "," + str(thirdSide), "form an isosceles right triangle")
    elif (firstSide - marginOfError) <= (((secondSide ** 2) + (thirdSide ** 2) **1/2)):
        print(str(firstSide) + "," + str(secondSide) + "," + str(thirdSide), "form an isosceles right triangle")
else:
    print("The triangle is not isosceles and is not and equilateral")

