def search(list, object):
    sequence = 0
    for items in list:
        if items == object:
            return True, sequence
        else:
            sequence += 1
    return False

print(search([1,2,3,4,5], 3))