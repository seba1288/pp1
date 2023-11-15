
def detector(detect):
    persons = 0
    for action in detect:
        if action == "+":
            persons += 1
        else:
            persons -= 1
        if persons >= 3:
            return True
        
    return False


print(detector("+-+++-+---"))
print(detector("+-+-+-+-"))
print(detector('+-++-+--' ))
print(detector("+-++-++-+---"))