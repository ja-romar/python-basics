import unittest

from unit import substraction

class TestSubstraction(unittest.TestCase):
    def test1(self):
        self.assertEqual(substraction(2,1), 1) #Test when is tested 2 - 1 shoul return 1


unittest.main()