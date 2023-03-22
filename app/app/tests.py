"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_number(self):
        res = calc.subtract(10, 15)

        self.assertEquals(res, 5)
