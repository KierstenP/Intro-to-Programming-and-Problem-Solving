character = str(input("Please enter a character: "))
ordinal = ord(character)
if 65 <= ordinal <= 90:
    print(character, "is an upper case letter.")
elif 97 <= ordinal <= 122:
    print(character, "is a lower case letter.")
elif 48 <= ordinal <= 57:
    print(character, "is a digit.")
else:
    print(character, "is a non-alphanumeric character.")
