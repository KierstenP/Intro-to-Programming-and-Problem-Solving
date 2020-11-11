def reverse_to_new_list(lst):
    newList = []
    for i in lst:
        newList.insert(0, i)

    return newList

def reverse_in_place(lst):
    for i in range(len(lst)):
        currentItem = lst[len(lst)-1]
        lst.insert(i, currentItem)
        lst.pop()

    return lst
