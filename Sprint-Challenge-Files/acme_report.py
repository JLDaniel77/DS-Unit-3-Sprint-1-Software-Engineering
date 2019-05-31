"""Report to track inventory."""

import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Function for generating a random list of products"""
    products = []
    for _ in range(1, num_products + 1):
        s = ' '
        name = s.join(random.sample(ADJECTIVES, 1)
                      + random.sample(NOUNS, 1))
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name=name, price=price, weight=weight,
                          flammability=flammability)
        products.append([product.name, product.price, product.weight,
                        product.flammability])
    return products


def inventory_report(products):
    """
    Function to generate an inventory report from a list of
    products
    """
    names = [i[0] for i in products]
    price = [i[1] for i in products]
    weight = [i[2] for i in products]
    flammability = [i[3] for i in products]

    name_count = len(set(names))
    price_mean = round(sum(price) / len(price), 2)
    wgt_mean = round(sum(weight) / len(weight), 2)
    flam_mean = round(sum(flammability) / len(flammability), 2)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Number of unique product names:', name_count)
    print('Average price:', price_mean)
    print('Average weight', wgt_mean)
    print('Average flammability', flam_mean)


if __name__ == '__main__':
    inventory_report(generate_products())
