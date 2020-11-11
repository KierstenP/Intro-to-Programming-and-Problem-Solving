line = input("Please enter a line of text: ")
ch = input("Please enter the character you want to remove: ")
newLine = ""
for i in line:
    if i != ch:
        newLine += i
    else:
        newLine += ""
print(newLine)
