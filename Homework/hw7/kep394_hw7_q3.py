def add_list(lst1, lst2):
    addedList = []
    firstListValue = 0
    secondListValue = 0

    for i in range(len(lst1)):
        firstListValue = lst1[i]
        secondListValue = lst2[i]
        addedList.append(firstListValue+secondListValue)

    return addedList

def get_list():
    flag = True
    lst = []
    while flag == True:
        userInput = input()
        if userInput == "done":
            flag = False
        else:
            lst.append(int(userInput))
    return lst

def main():
    print("Please enter a list of numbers, type 'done' when finished")
    lst1 = get_list()

    print("Please enter a second list of numbers, type 'done' when finished")
    lst2 = get_list()

    if len(lst1)==len(lst2):
        for i in add_list(lst1, lst2):
            print(i)

    else:
        print("Lists are different lengths. ")


