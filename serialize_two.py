import json
data = {
    'firstname': 'Ahmad',
    'lastname' : 'maulana',
    'age' : 26,
    'hobbies' : ['swimming', 'progamming']
}

file = open("data.json", "w")
json.dumps(data, file)