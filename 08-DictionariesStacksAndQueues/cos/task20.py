import json

f = open('euro.json','r')
exchange = json.load(f)
print(exchange)

print('Date     Buing Rate       Selling Rate ')
print('=======================================')
for dict in exchange["rates"]:
    print(f'{dict["effectiveDate"]}     {dict["bid"]}     {dict["ask"]}')
      
