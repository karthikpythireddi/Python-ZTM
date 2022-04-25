#In Python Lists are kind of Arrays, a collection of items

amazon_cart = ['notebooks',
    'sunglasses',
    'toys',
    'grapes'
]


amazon_cart[0] = 'laptop'

newcart = amazon_cart[:]

newcart[0] = 'gummies'

print(amazon_cart)

print(newcart)

