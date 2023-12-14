import json

lim = {}
f = open('students.json','r')
Json = json.load(f)

keys = list(Json[0])
print(keys)
keys1 = [ 'gender', 'age', 'year_of_study', 'email']
for i in Json:
    for key in keys1:
        i.pop(key)
print(Json)
