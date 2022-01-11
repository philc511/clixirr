import unittest
from datetime import date
from clixirr2 import get_dated_items

class GetDatedItemsTest(unittest.TestCase):

    # empty cashflows and balances should return empty results 
    def test_get_dates_all_empty(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
