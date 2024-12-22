
product = []
while True:
    name = input('Please input the name of the product (type "q" to leave): ')
    if name == 'q':
        print('Leave the function. Thank you!')
        break
    price = input('Please input the price of the product: ')
    product.append([name, price])

print('You input', len(product), 'item(s)')
print('Here is your list:', product)

for p in product:
    print('The price of', p[0], 'is', p[1])