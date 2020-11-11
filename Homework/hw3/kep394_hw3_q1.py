weightInPounds = int(input("Please enter a weight in pounds: "))
heightInInches = int(input("Please enter a height in inches: "))
weightInKilograms = (weightInPounds * 0.453592)
heightInMeters = (heightInInches * 0.0254)
bmi = weightInKilograms/(heightInMeters * heightInMeters)
print("BMI is:", bmi)
if bmi < 18.5:
    print("Your weight status is underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your weight status is normal.")
elif bmi >= 25 and bmi <= 29.9:
    print("Your weight status is overweight.")
else:
    print("Your weight status is obese")
