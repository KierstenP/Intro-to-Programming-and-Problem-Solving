password = input("Enter a password: ")
upperCount = 0
lowerCount = 0
digitCount = 0
specialCount = 0
for i in password:
    if i.isupper():
        upperCount += 1
    elif i.islower():
        lowerCount += 1
    elif 48 <= ord(i) <= 57:
        digitCount += 1
    elif ord(i) == 33 or 35 <= ord(i) <= 36 or ord(i) == 64:
        specialCount += 1
if upperCount >= 2 and lowerCount >= 1 and digitCount >= 2 and specialCount >= 1:
    print(password, "is a valid password.")
else:
    print(password, "is not a valid password.")


