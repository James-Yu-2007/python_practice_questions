import heapq

def mostFreqNum(list, k):
    dict = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
    for row in list:
        for num in row:
            if num == 1:
                dict['1'] += 1
            elif num == 2:
                dict['2'] += 1
            elif num == 3:
                dict['3'] += 1
            elif num == 4:
                dict['4'] += 1
            elif num == 5:
                dict['5'] += 1
            elif num == 6:
                dict['6'] += 1
    n = []
    for temp in dict.values():
        n.append(temp)
    for temp2 in dict.keys():
        n.append(int(temp2))
    mostFreqNum = []
    for i in range(k):
        mostFreqNum.append(n[n.index(max(n[:5]))+6])
        n.remove(max(n))
    return mostFreqNum

list = [
    [1,2,3],
    [1,2],
    [1,2,3,4],
    [1,2,3,4,5,6],
    [1,2,3,4,5],
    [1]
]

print(mostFreqNum(list, 2))