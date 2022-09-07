import json
json_obj =  '{ "Name":"James", "Grade":90, "Age":15 }'
python_obj = json.loads(json_obj)
print(python_obj)