list = [3,6,2,5,1,4]

def selectionSort(List):
    list = []
    for k in List:
        list.append(k)
    for i in range(len(list)):
        n = -1
        for j in list:
            n += 1
            if j == min(list):
                index = n
        List[i] = list[index]
        list.remove(list[index])
        
    return List

print(selectionSort(list))