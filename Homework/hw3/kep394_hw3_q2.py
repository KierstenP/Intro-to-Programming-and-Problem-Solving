priceOne = float(input("Enter price of first item: "))
priceTwo = float(input("Enter price of second item: "))
membershipStatus = input("Does customer have a club card? (Y/N): ")
taxRate = (float(input("Enter tax rat, e.g. 5.5 for 5.5% tax: "))) / 100
basePrice = priceOne + priceTwo
finalDiscount = 0
totalPrice = 0
if priceOne > priceTwo:
    discountOne = (priceTwo * .5)
    if membershipStatus == "Y":
        finalDiscount = (discountOne + priceOne) * .9
        totalPrice = round(((finalDiscount * taxRate) + finalDiscount), 2)
    elif membershipStatus == "N":
        finalDiscount = (discountOne + priceOne)
        totalPrice = round(((finalDiscount * taxRate) + finalDiscount), 2)
elif priceOne < priceTwo:
    discountOne = (priceOne * .5)
    if membershipStatus == "Y":
        finalDiscount = (discountOne +priceTwo) * .9
        totalPrice = round(((finalDiscount * taxRate) + finalDiscount), 2)
    elif membershipStatus == "N":
        finalDiscount = (discountOne + priceTwo)
        totalPrice = round(((finalDiscount * taxRate) + finalDiscount), 2)
print("Base price is:", basePrice)
print("Price after discounts =", finalDiscount)
print("Total Price =", totalPrice)