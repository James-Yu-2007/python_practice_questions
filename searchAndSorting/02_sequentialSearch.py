def sequentialSearch(list, item):
    sequence = 0
    for data in list:
        if item == data:
            return True, sequence
        else:
            sequence += 1
    return False

print(sequentialSearch([5,2,3,1,4], 3))