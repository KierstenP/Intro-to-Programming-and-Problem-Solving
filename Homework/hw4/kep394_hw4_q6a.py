lengthOfSequence = int(input("Pleas enter the length of the sequence: "))
sum = 0
print("Please enter your sequence: ")
for i in range(lengthOfSequence):
    sequence = int(input(""))
    sum += sequence
print("The geometric mean is:", round((sum ** (1 / lengthOfSequence)), 4))
