thisdict = {"name":"KOPE SOLO DEVELOPER", "age":15}
print(thisdict["name"])
print(thisdict.get("name"))

print(thisdict.keys())
print(thisdict.values())

thisdict.update({"age":16})
print("update age : ", thisdict.values())

thisdict.pop("age")
print("pop age : ",thisdict)