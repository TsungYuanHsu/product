# This is a product recorder

import os

# product = []

# # Check file is present
# if os.path.isfile('product.csv'):
#     print('File is present')
    
#     # Read the existing file
#     with open('product.csv', 'r', encoding = 'utf-8') as f:
#         for line in f:
#             if 'Name,Price' in line:
#                 continue
#             product.append(line.strip().split(','))
#     print(product)    

# else:
#     print('File is not present')

# # Let user input item
# while True:
#     name = input('Please input the name of the product (type "q" to leave): ')
#     if name == 'q':
#         print('Leave the function. Thank you!')
#         break
#     price = input('Please input the price of the product: ')
#     product.append([name, price])

# print('You input', len(product), 'item(s)')
# print('Here is your list:', product)

# # Print all the items
# for p in product:
#     print('The price of', p[0], 'is', p[1])

# # Write items in csv file
# with open('product.csv', 'w', encoding = 'utf-8') as f:
#     f.write('Name' + ',' + 'Price' + '\n')
#     for p in product:
#         f.write(p[0] + ',' + p[1] + '\n')

# Read the existing file
def read_file(filename):
    product = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'Name,Price' in line:
                continue
            product.append(line.strip().split(','))
    return product

# Let user input item
def user_input(product):
    while True:
        name = input('Please input the name of the product (type "q" to leave): ')
        if name == 'q':
            print('Leave the function. Thank you!')
            break
        price = input('Please input the price of the product: ')
        product.append([name, price])

    print('You input', len(product), 'item(s)')
    print('Here is your list:', product)
    return product

# Print all the items
def print_prodcuts(product):
    for p in product:
        print('The price of', p[0], 'is', p[1])

# Write items in csv file
def write_file(filename, product):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('Name' + ',' + 'Price' + '\n')
        for p in product:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'product.csv'
    if os.path.isfile(filename):
        print('File is present')
        product = read_file(filename)
        print(product) 
    else:
        print('File is not present')
    product = user_input(product)
    print_prodcuts(product)
    write_file(filename, product)

main()
