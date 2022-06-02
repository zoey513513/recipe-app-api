#  django test
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """ Test the calc module """
    def test_add_number(self): # unit testing, focuses on unit functionality
        """ Test addn function. """
        res = calc.add(5,6)
        self.assertAlmostEqual(res,11)
    def test_substract_numbers(self): # Test-driven development (TDD), focuses on design and testability
        res = calc.subtract(10,15)
        self.assertAlmostEqual(res,-5)

