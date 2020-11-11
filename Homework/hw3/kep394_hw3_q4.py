a = float(input("Please enter a value of a: "))
b = float(input("Please enter a value of b: "))
c = float(input("Please enter a value of c: "))
if a == 0 and b == 0 and c == 0:
    print("This equation has an infinite number of solutions.")
elif a == 0 and b == 0:
    print("This equation has no solution.")
elif b == 0 and c > 0:
    print("This equation has no solution")
else:
    squareRoot = ((b ** 2) - (4 * a * c)) ** (1 / 2)
    solutionOne = (-b) / (2 * a)
    if squareRoot == 0:
        print("This equation has a single real solution x=" + str(solutionOne))
    else:
        solutionTwo = ((-b) - squareRoot) / (2 * a)
        print("This equation has two real solutions, x=" + str(solutionOne), "and x=" + str(solutionTwo))
