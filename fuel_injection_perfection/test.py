import unittest
from solution import solution


class TestFuelInjectionPerfection(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(4), 2)

    def test_2(self):
        self.assertEqual(solution(15), 5)


if __name__ == '__main__':
    unittest.main()
