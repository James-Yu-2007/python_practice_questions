def bubbleSort(list):
    for n in range(len(list)-1):
        for l in range(n):
            if list[l]>list[l+1]:
                temp = list[l]
                list[l] = list[l+1]
                list[l+1] = temp
            print(list)

list = [3,6,2,5,1,4]
bubbleSort(list)
print(list)