import unittest
from solution import solution


class TestFuelInjectionPerfection(unittest.TestCase):    
    def test_1(self):
        self.assertEqual(solution('3'), 2)

    def test_2(self):
        self.assertEqual(solution('2'), 1)
    
    def test_3(self):
        self.assertEqual(solution('4'), 2)

    def test_4(self):
        self.assertEqual(solution('15'), 5)
    
    def test_5(self):
        self.assertEqual(solution('34'), 6)


if __name__ == '__main__':
    unittest.main()
