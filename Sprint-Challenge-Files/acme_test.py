#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_new_product(self):
        """Test sealability and explode methods with new values"""
        prod = Product(name='New Product', price=100, weight=60,
                       flammability=0.9)
        self.assertEqual(prod.explode(), '...BABOOM!!')
        self.assertEqual(prod.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):
    """Making sure the report is accurate."""

    def test_default_num_products(self):
        """Confirm report generates 30 products."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Confirm that all product names are valid"""
        names = [i[0] for i in generate_products()]

        for n in names:
            name = str(n).split()
            name1 = name[0]
            name2 = name[1]
            self.assertIn(name1, ADJECTIVES)
            self.assertIn(name2, NOUNS)


if __name__ == '__main__':
    unittest.main()
