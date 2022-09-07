import json
dict = {'4': 5, '6': 7, '1': 3, '2': 4}
print(json.dumps(dict, sort_keys=True))