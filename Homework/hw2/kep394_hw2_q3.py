import math
import turtle
legOne = float(input("Please enter the length of one side of a triangle: "))
legTwo = float(input("Please enter the length of another side of a triangle: "))
angle = float(input("Please enter the angle between the two lengths given: "))
angleRadians = math.radians(angle)
cosAngle = math.cos(angleRadians)
hypotenuseSquared = ((legOne * legOne) + (legTwo * legTwo) - (2 * legOne * legTwo * cosAngle))
hypotenuse = math.sqrt(hypotenuseSquared)
angleTwo = math.sinh((math.sin(angleRadians) * legOne) / hypotenuse)
angleTwoDegrees = math.degrees(angleTwo)
turnOne = (180 - angle)
turnTwo = (180 - angleTwoDegrees)
turtle.forward(legOne)
turtle.left(turnOne)
turtle.forward(legTwo)
turtle.left(turnTwo)
turtle.forward(hypotenuse)
turtle.done()