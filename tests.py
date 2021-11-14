import unittest
from datetime import date
from clixirr2 import get_dates

class TestStringMethods(unittest.TestCase):

    @staticmethod
    def dummy_fn(items):
        return sum([t[1] for t in items])
       
    # empty cashflows and balances should return empty results 
    def test_get_dates_all_empty(self):
        self.assertEqual(get_dates([], [], self.dummy_fn), [])

    # empty cashflows and non-empty balances should return empty results
    def test_get_dates_empty_cashflows(self):
        self.assertEqual(get_dates([], [['2021-01-01',100.0]], self.dummy_fn), [])

    # non-empty cashflows and empty balances should return empty results
    def test_get_dates_empty_balances(self):
        self.assertEqual(get_dates([['2021-01-01',100.0]], [], self.dummy_fn), [])

    # 1 cashflows and 1 balance should return one result
    def test_get_dates_one_balances(self):
        start = date(2020, 1, 2)
        end = date(2021, 3, 4)
        results = get_dates([[start, -10.0]], [[end, 15.0]], self.dummy_fn)
        self.assertEqual(results, [[start, end, 5.0]])

    # cashflows:
    # 2020-02-01 1
    # 2020-06-17 2
    # 2021-05-03 4
    # balances:
    # 2020-07-01 8
    # 2021-08-21 16
    # Should give two results, 
    # 2020-02-01->2020-07-01 7
    # 2020-07-01->2021-08-21 12

    # two cashflows on same day

    # two balances on the same day

    # cashflow same day as balance
    

if __name__ == '__main__':
    unittest.main()
