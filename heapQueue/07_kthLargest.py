import heapq

def kthLargest(k, heap):
    heapq.heapify(heap)
    for i in range(k):
        kth = heapq.heappop(heap)
    return kth

print(kthLargest(3, [3,2,5,1,4,6]))