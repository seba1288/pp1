name = "Sebastian Wróbel"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt",'w')
file.write(name+"\n")
file.write(university+"\n")
file.write(field+"\n")
file = open('student.txt','r')
file1 = file.read()
print(file1)
file.close()
