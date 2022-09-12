import heapq

def maxProOf3(heap):
    threeLargest = heapq.nlargest(3, heap)
    return(threeLargest[0] * threeLargest[1] * threeLargest[2])

print(maxProOf3([1,2,3,4,5,6]))