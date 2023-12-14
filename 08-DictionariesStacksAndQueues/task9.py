

countries = [
    {"name":"Poland", "population":38000000},
    {"name":"German", "population":80000000},
    {"name":"French", "population":100000000},
    {"name":"Russia", "population":380000000000},
    {"name":"Italy", "population":7000000000},
]
n = 0
print('COUNTRY','POPULATION')
while n < len(countries):
    print(countries[n]['name'],countries[n]['population'])
    n += 1
