print("Enter number in the simplified Roman system: ")
romanNum = int(input())
changeNum = romanNum
mValue = changeNum // 1000
changeNum = changeNum % 1000
dValue = changeNum // 500
changeNum = changeNum % 500
cValue = changeNum // 100
changeNum = changeNum % 100
lValue = changeNum // 50
changeNum = changeNum % 50
xValue = changeNum // 10
changeNum = changeNum % 10
vValue = changeNum // 5
changeNum = changeNum % 5
iValue = changeNum // 1
changeNum = changeNum % 1
print()
print(romanNum, "is", ("M" * mValue) + ("D" * dValue) + ("C" * cValue) + ("L" * lValue) + ("X" * xValue)
      + ("V" * vValue) + ("I" * iValue))
