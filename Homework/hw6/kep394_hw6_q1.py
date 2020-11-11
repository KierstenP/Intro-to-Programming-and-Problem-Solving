def print_shifted_triangle(n, m, symbol):
    numberOfSpaces = m + (n - 1)
    numberOfSymbols = 1
    for i in range(n):
        print((" " * numberOfSpaces), (symbol * numberOfSymbols), sep="")
        numberOfSpaces -= 1
        numberOfSymbols += 2
        print()

def print_pine_tree(n, symbol):
    newN = 2
    m = n-1
    for i in range(n):
        print_shifted_triangle(newN, m, symbol)
        newN += 1
        m -= 1

def main():
    n = int(input("How many triangles will be in the tree? "))
    symbol = str(input("What character will fill the tree? "))
    print_pine_tree(n, symbol)

main()