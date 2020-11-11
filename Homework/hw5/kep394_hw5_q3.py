expression = str(input("Enter a mathematical expressions. "))
lengthOfExpression = len(expression)
firstSpace = expression.find(" ")
secondSpace = (expression[firstSpace+1:(lengthOfExpression+1)]).find(" ")
operand1 = int(expression[0:firstSpace])
op = ord(expression[firstSpace+1])
operand2 = int((expression[firstSpace+1:(lengthOfExpression+1)])
               [secondSpace+1:((len(expression[firstSpace+1:(lengthOfExpression+1)]))+1)])
if op == 42:
    print(expression, "=", (operand1 * operand2))

elif op == 43:
    print(expression, "=", (operand1 + operand2))

elif op == 45:
    print(expression, "=", (operand1 - operand2))

elif op == 47:
    print(expression, "=", (operand1 / operand2))