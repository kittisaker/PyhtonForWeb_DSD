# read jason
import json

with open("sample1.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))

print(data.keys())
print(data.values())