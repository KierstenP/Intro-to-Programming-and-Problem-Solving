word = input("Enter a word: ")
vowelCount = 0
consonantCount = 0
for i in word:
    if  i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "a" \
            or i == "e" or i == "i" or i == "o" or i == "u":
        vowelCount += 1
    else:
        consonantCount += 1
print(word, "has", vowelCount, "vowels and", consonantCount, "consonants.")
