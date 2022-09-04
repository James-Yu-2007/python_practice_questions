list = [3,6,2,5,1,4]

def minimum(list):
    smallest = None
    for i in list:
        if smallest:
            if i < smallest:
                smallest = i
        else:
            smallest = i
    return smallest

def indexOfMin(list):
    index = -1
    for i in list:
        index += 1
        if i == minimum(list):
            return index

def selectionSort(list):
    for i in range(len(list)):
        n = list[i]
        list[i] = list[indexOfMin(list[i:]) + i]
        list[indexOfMin(list[i:]) + i] = n
    return list

print(selectionSort(list))