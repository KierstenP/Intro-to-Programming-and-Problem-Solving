class BinaryPositiveInteger:
    def __init__(self, num=0):
        binaryNumber = ""

        while num > 0:
            if num % 2 == 0:
                binaryNumber += "0"
            else:
                binaryNumber += "1"
            num = num // 2

        self.num = binaryNumber[::-1]

    def __add__(self, other):
        addedBinary = BinaryPositiveInteger()
        length1 = len(self.num)
        length2 = len(other.num)
        carry = 0
        sum = 0
        answer = ""
        if length1 > length2:
            maxLength = length1
            other.num = ("0" * (length1 - length2)) + other.num
        else:
            maxLength = length2
            self.num = ("0" * (length2 - length1)) + self.num
        for i in range(maxLength-1, -1 , -1):
            sum = carry
            if self.num[i] == "1":
                sum += 1
            if other.num[i] == "1":
                sum += 1
            if sum % 2 == 1:
                answer = "1" + answer
            else:
                answer = "0" + answer
            if sum >= 2:
                carry = 1
            else:
                carry = 0
        if carry != 0:
                answer = "1" + answer
        sum = 0
        addedBinary.num = answer
        return "0b" + addedBinary.num

    def __lt__(self, other):
        binary1 = self.num
        binary2 = other.num
        if len(binary1) > len(binary2):
            return False
        elif len(binary2) > len(binary1):
            return True
        elif len(binary1) == len(binary2):
            for i in range(len(binary1)):
                if binary1[i] == "1" and binary2[i] == "0":
                    return False
                elif binary2[i] == "1" and binary1[i] == "0":
                    return True

    def is_power_of_two(self):
        oneCounter = 0
        for i in self.num:
            if i == "1":
                oneCounter += 1
        if oneCounter == 1:
            return True
        else:
            return False

    def largest_power_of_two(self):
        highestPowerOfTwo = 2**((len(self.num))-1)
        return highestPowerOfTwo

    def __repr__(self):
        return "0b" + self.num


#these are just to check that the code works
#n1 = BinaryPositiveInteger(13)
#print(n1)
#n2 = BinaryPositiveInteger(25)
#print(n2)
#print(n1.is_power_of_two())
#print(n1.largest_power_of_two())
#print(n1<n2)
#print(n1 + n2)



