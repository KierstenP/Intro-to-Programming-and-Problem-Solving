import random
def create_permutation(n):
    list = []
    currentNumber = 0
    for i in range(n):
        list.append(i)
    for ind in range(n):
        currentNumber = list.pop(ind)
        currentRandom = random.randint(0, n - 2)
        removedNumber = list[currentRandom]
        list[currentRandom] = currentNumber
        list.append(removedNumber)
    return list

def scramble_word(word):
    lengthOfWord = len(word)
    newWord = ""
    permutation = create_permutation(lengthOfWord)
    for i in permutation:
        newWord += word[i]
    return(newWord)


def main():
    fileIn = open("hw8 - word bank.txt", "r")
    listOfWords = fileIn.readlines()
    lengthOfList = len(listOfWords)
    randomPlace = random.randint(0, lengthOfList)
    word = listOfWords[randomPlace]
    scrambledWord = scramble_word(word)
    print("Unscramble the word:", scrambledWord, end = "")
    correctGuess = False
    for i in range (1, 4):
        guess = input("Try #" + str(i) + ": ")
        if guess == word:
            print("Yay you got it!")
            correctGuess = True
            break
        else:
            print("Wrong!")
    if correctGuess == False:
        print("You are out of tries! The word was", word)



main()
