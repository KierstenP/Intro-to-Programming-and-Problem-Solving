print("Please enter a non-empty sequence of positive integers, each one in a separate line. End")
print("your sequence by typing done: ")
lengthOfSequence = 0
sum = 0
userInput = 0
while input != "done":
    userInput = str(input(""))
    if userInput=="done":
        print("The geometric mean is:", round(sum ** (1 / lengthOfSequence), (4)))
    else:
        userInput = int(userInput)
        sum += userInput
        lengthOfSequence += 1