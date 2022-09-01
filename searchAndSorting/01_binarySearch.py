def binary_search(list, item):
    if not list:
        return False

    midpoint = len(list) // 2
    if list[midpoint] == item:
        return True

    if item < list[midpoint]:
        return binary_search(list[:midpoint], item)

    return binary_search(list[midpoint + 1:], item)

print(binary_search([1,2,3,4,5], 3))