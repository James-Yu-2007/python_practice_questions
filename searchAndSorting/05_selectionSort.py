list = [3,6,2,5,1,4]

def selectionSort(list):
    for i in range(len(list)):
        minimum = None
        for j in list[i:]:
            if minimum:
                if j < minimum:
                    minimum = j
            else:
                minimum = j
        index = -1
        for k in list:
            index += 1
            if k == minimum:
                break
        n = list[i]
        list[i] = list[index]
        list[index] = n
    return list

print(selectionSort(list))