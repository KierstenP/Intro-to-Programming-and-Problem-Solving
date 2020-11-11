inputString = input("Enter an odd length string: ")
midChrPosition = int(((len(inputString)+1)/2)-1)
if (len(inputString) % 2) != 0:
    print("Middle character:", inputString[midChrPosition])
    print("First half:", inputString[0:midChrPosition])
    print("Second half:", inputString[midChrPosition+1:(len(inputString)+1)])
else:
    print("The entered string is not of odd length!")
