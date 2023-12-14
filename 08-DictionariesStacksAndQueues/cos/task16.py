
def hotel_list(hotels):
    list_h = []
    for i in hotels:
        list_h.append(i['name'])
    return list_h
def avg_price(hotels):
    suma_p = 0
    for i in hotels:
        suma_p += i['price']
    average = suma_p/len(hotels)
    return round(average)
    


Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00},
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
hotels_1 = Hotels_in_Krakow + hotels_in_Sopot
print(hotel_list(hotels_1))
print(avg_price(hotels_1))
