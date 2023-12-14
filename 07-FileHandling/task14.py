file = open("shopping.txt",'w')
read_product = True
counter = 0
while counter < 5:
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(product + '\n')
    else:
        read_product = False
file = open('shopping.txt','r')
print(file.read())
file.close()
