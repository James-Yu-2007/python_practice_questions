import json

with open('json.json') as f:
    data = json.loads(f)

for info in data:
    del info['name']

with open('newJson.json', 'w')as f:
    json.dump(data, f)