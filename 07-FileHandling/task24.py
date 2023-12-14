import csv

with open('studentslist.csv','r')as file:
    reader = csv.DictReader(file)

    for i in reader:
        age = i['age']
        if int(age) < 30:
            
            print(i['first_name'],i['last_name'],i['email'])

