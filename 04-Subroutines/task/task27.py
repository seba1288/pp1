import string

def card_number(card):
    card = str(card)
    card_chage = card[0:2] + "**********" + card[-4:]
    return card_chage


print(card_number(1234567890111111))
print(card_number(5290312400019022))
    

