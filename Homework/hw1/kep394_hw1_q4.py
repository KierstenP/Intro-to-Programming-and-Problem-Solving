year = int(input("Enter a year which you like to know the estimated population of: "))
newYear = int(year - 2017)
newYearSeconds = int(newYear * 31536000)
numberOfBirths = int(newYearSeconds / 7)
numberOfDeaths = int(newYearSeconds / 13)
numberOfImmigrants = int(newYearSeconds / 35)
estimatedPopulation = int(307357870 + numberOfBirths - numberOfDeaths + numberOfImmigrants)
print("In the year", year, "there will be an estimated population of", estimatedPopulation,'.')