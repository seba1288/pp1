basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}
thisdict = {}
for k,v in basic_data.items():
    thisdict.update({k:v})
for k,v in advanced_data.items():
    thisdict.update({k:v})

print(thisdict)

    