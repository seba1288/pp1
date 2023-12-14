import json

student = {
    "name": 'Seba',
    "surname": 'Wrona',
    "age": 19,
    "course": 'AI',
    "year": 1,
    "has-library-card": True
}
x = json.dumps(student)
f = open('student.json','w')
f.write(x)
f.close()

