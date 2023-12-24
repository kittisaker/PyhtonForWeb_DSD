# write json
import json

person_dict = {"name": "Bobby", "age":15}

# person_json = json.dumps(person_dict)
# print(type(person_dict))

with open("sample2.json", "w") as json_file:
    json.dump(person_dict, json_file)