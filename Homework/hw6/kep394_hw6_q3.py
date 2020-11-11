def return_first_word(expression):
    firstSpacePosition = expression.find(" ")
    return expression[: firstSpacePosition]

def take_out_phrase(expression):
    firstSpacePosition = expression.find(" ")
    return expression[firstSpacePosition+1: len(expression)+1]

def reverse_sentence(expression):
    numberOfWords = 0
    for i in expression:
        if ord(i) == 32:
            numberOfWords += 1
    oldExpression = ""
    for i in range(numberOfWords):
        word = return_first_word(expression)
        word += " "
        sentence = word + oldExpression
        oldExpression = sentence
        expression = take_out_phrase(expression)
    expression += " "
    reversedSentence = expression + oldExpression
    return reversedSentence

def main():
    expression = str(input("Please give me a phrase: "))
    print(reverse_sentence(expression))

main()




