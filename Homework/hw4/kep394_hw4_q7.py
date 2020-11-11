import random
number = random.randint(1, 100)
range1 = 1
range2 = 100
guess = False
guessesLeft = 5
theirGuess = 0
guessCount = 0
print("I thought of a number between", range1, "and", range2, "! Try to guess it.")
while guess == False and guessesLeft > 0:
    guessesLeft -= 1
    guessCount += 1
    print()
    print("Range:[", range1,",", range2,"], Number of guesses left:", guessesLeft + 1)
    theirGuess = int(input("Your guess: "))
    if theirGuess == number:
        print("Congrats! You guessed my number in", guessCount, "guesses.")
        guess = True
    elif theirGuess > number:
        if guessesLeft > 0:
            print("Wrong! My number is smaller.")
            range2 = theirGuess
        elif guessesLeft == 0:
            print("Out of guesses! My number is", number)
    elif theirGuess < number:
        if guessesLeft > 0:
            print("Wrong! My number is bigger.")
            range1 = theirGuess
        elif guessesLeft == 0:
            print("Out of guesses! My number is", number)