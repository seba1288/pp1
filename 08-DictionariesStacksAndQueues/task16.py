Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]


def hotel_list(hotels):
    result = []
    for dict  in hotels:
        print(dict['name'],end=',')

def avg_price(hotels):
    suma = 0
    count = 0
    for dic in hotels:
        suma += dic['price']
        count += 1
    return round(suma/count,0)

def avg_price_diff(hotels,hotels2):
    
    if avg_price(hotels) > avg_price(hotels2):
        return f"{hotels} are cheper and price is {avg_price(hotels)}"
    else:
        return f"{hotels2} are cheper and price is {avg_price(hotels2)}"


print(hotel_list(hotels_in_Sopot))
print(hotel_list(Hotels_in_Krakow))
print(avg_price(hotels_in_Sopot),avg_price(Hotels_in_Krakow))
print(avg_price_diff(hotels_in_Sopot,Hotels_in_Krakow))
