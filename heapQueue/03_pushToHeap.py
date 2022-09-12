import heapq

list = [1,2,3,4,5,6]
heap = []
for n in list:
    heapq.heappush(heap, n)
for i in range(len(heap)):
    print(heapq.heappop(heap))