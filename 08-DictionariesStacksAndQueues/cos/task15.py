basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}
person = {

}


for key,val in basic_data.items():
    person.update({key:val})
for key,val in advanced_data.items():
    person.update({key:val})

print(person)