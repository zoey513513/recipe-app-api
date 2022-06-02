#  django test
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    def test_add_number(self): 
        res = calc.add(5,6)
        self.assertAlmostEqual(res,11)
    def test_substract_numbers(self):
        res = calc.subtract(10,15)
        self.assertAlmostEqual(res,-5)
