letterString = input("Please enter a string of lowercase letters: ")
previousCharacter = ""
increasing = True
for i in letterString:
    currentCharacter = i
    if currentCharacter > previousCharacter:
        previousCharacter = currentCharacter
    else:
        increasing = False
if increasing == True:
    print(letterString, "is increasing.")
else:
    print(letterString, "is not increasing.")
