import json
data = {
    'firstname': 'Ahmad',
    'lastname' : 'maulana',
    'age' : 26,
    'hobbies' : ['swimming', 'progamming']
}

data_json = json.dumps(data, indent=3)
print(data_json)