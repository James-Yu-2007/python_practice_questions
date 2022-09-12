import heapq
heap = [6,5,4,3,2,1]
heapq.heapify(heap)
orderedHeap = []
for i in range(len(heap)):
    orderedHeap.append(heapq.heappop(heap))
print(orderedHeap)