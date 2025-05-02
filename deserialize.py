import json

data_json = """ 
{
    "firstname" : "Ahmad",
    "lastname" : "maulana",
    "age" : 26
    "hobbies" : ["swimming","progamming"]
}
"""
data_python = json.loads(data_json)
print(type(data_python))