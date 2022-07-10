input = input("please input your list of numbers seprated by commas: ")
input = input.replace(' ', '')
input = input.replace('[', '')
input = input.replace(']', '')
listInput = input.split(',')
endPoint = 0
while endPoint < len(listInput):
    subList = listInput[0: (len(listInput)-endPoint)]
    endPoint = endPoint + 1
    y = 0
    for x in subList:
        subList2 = subList[y: int(len(subList))]
        b = 0
        for a in subList2:
            b = b+int(a)
        if b == 0:
            print(subList2)

        y = y+1