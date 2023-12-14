def f(p1,p2):
    count_p1 = 0
    count_p2 = 0
    for i in p1:
        count_p1 += If(i)
    for i in p2:
        count_p2 += If(i)
    if count_p1 > count_p2:
        return True
    else:
        return False







def If(card):
    points = 0
    if str(card) == 'A' or 'J' or 'K' or 'T':
        points += 10
    else:
        card = int(card)
        points += card
    return points

print(f("AJ972","AQT72"),f("9532","K8"),f("987","AT4")  )