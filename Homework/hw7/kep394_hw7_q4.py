def create_prefix_lists(lst):
    bigList = []
    for i in range(len(lst)+1):
        bigList.append(lst[0:i])

    return bigList