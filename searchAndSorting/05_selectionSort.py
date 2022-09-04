list = [3,6,2,5,1,4]

def selectionSort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                n = list[i]
                list[i] = list[j]
                list[j] = n
    return list

print(selectionSort(list))