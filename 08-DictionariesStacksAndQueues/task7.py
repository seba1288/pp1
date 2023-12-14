dict1 = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(dict1)
print(dict1["name"])
print(dict1["hobby"])
dict1["surname"] = "Nowak"
print(dict1["surname"])
dict1["married"] = not dict1["married"]
dict1["hobby"].append("bicycle")

print(dict1)
dict1.update({'gender':'male'})
dict1.update({'hobby':["swimming","",'bicycle']})
dict1['phone']['workphone'] = '313131444'
print(dict1)




