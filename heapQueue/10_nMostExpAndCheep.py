import heapq
items = [
    {'name': '1', 'price': 1},
    {'name': '2', 'price': 2},
    {'name': '3', 'price': 3},
    {'name': '4', 'price': 4},
    {'name': '5', 'price': 5},
    {'name': '6', 'price': 6}
]
list = []
for row in items:
    list.append(row['price'])
cheap = heapq.nsmallest(3, list)
expensive = heapq.nlargest(3, list)
print(expensive, cheap)
