import unittest
from matrox.elements.fraction import *

class TestFractionClass(unittest.TestCase):

    def test_create_whole_fraction(self):
        f = Fraction(1)
        self.assertEqual(f.get_num(), 1)
        self.assertEqual(f.get_den(), 1)
        self.assertEqual(str(f), "1")

    def test_create_fraction(self):
        f = Fraction(1, 2)
        self.assertEqual(f.get_num(), 1)
        self.assertEqual(f.get_den(), 2)
        self.assertEqual(str(f), "1/2")



class TestFraction(unittest.TestCase):
    
    def test_add_fractions(self):
        a = Fraction(2, 3)
        b = Fraction(4, 5)
        c = add_fractions(a, b)
        self.assertEqual(c.get_num(), 22)
        self.assertEqual(c.get_den(), 15)
        self.assertEqual(str(c), "22/15")

    def test_add_fractions_simplifiable(self):
        a = Fraction(3, 8)
        b = Fraction(3, 8)
        c = add_fractions(a, b, simplify=True)
        self.assertEqual(c.get_num(), 3)
        self.assertEqual(c.get_den(), 4)
        self.assertEqual(str(c), "3/4")