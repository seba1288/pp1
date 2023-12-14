import json

with open("jasonfile.json") as file:
    data = json.load(file)
    n = 1
for i in data:
    print(n)
    for key,value in i.items():
        print(f"{key} : {value}")
    n += 1
