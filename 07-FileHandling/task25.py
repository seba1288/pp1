import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
print(temperatures)
ave = 0
for i in temperatures:
    ave += int(i)

print(ave/len(temperatures))

