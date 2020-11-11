n = int(input("Please input a positive integer: "))
n1 = n
n2 = 1
space = 0
while (n1 > 0):
    print(str((" " * space) + ("*" * ((n1 * 2)-1))))
    n1-=1
    space+=1
for j in range(n, 0, -1):
    print(str((" " * (j - 1))) + ("*" * n2))
    n2+=2