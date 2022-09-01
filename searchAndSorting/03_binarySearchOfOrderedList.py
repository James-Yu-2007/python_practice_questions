def search(list, object):
    for items in list:
        if items == object:
            return True
    return False

print(search([1,2,3,4,5], 3))
print(search([1,2,3,4,5], 6))