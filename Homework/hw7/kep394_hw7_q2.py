def find_all(lst, val):

    valList = []

    for i in range(len(lst)):
        if lst[i]==val:
            valList.append(i)

    return valList