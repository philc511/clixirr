import unittest
from datetime import date
from clixirr2 import get_dates

class TestStringMethods(unittest.TestCase):

    def dummy_fn(items):
        return sum([t[0] for t in items])
        #return sum(items)
       
    # empty cashflows and balances should return empty results 
    def test_get_dates_all_empty(self):
        self.assertEqual(get_dates([], [], self.dummy_fn), [])

    # empty cashflows and non-empty balances should return empty results
    def test_get_dates_empty_cashflows(self):
        self.assertEqual(get_dates([], [['2021-01-01',100.0]], self.dummy_fn), [])

    # non-empty cashflows and empty balances should return empty results
    def test_get_dates_empty_balances(self):
        self.assertEqual(get_dates([['2021-01-01',100.0]], [], self.dummy_fn), [])

    # 1 cashflows and 1 balance should return empty results
    def test_get_dates_one_balances(self):
        start = date(2020, 1, 2)
        end = date(2021, 3, 4)
        self.assertEqual(get_dates([[start, -10.0]], [[end, 15.0]], self.dummy_fn), [[start, end, 5.0]])
 

if __name__ == '__main__':
    unittest.main()
