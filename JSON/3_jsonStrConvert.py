import json
python_obj = {
  "name": "James",
  "Grade": 90,
  "age": 15  
}
json_data = json.dumps(python_obj)
print(json_data)