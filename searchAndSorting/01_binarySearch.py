def binerySearch(list, data):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if data == list[mid]:
            found = True
        elif data > list[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return found

print(binerySearch([1,2,3,4,5,6], 3))