import unittest
from solution import solution


class TestExpandingNebula(unittest.TestCase):
    def test_1(self):
        input = [
            [True, False, True],
            [False, True, False],
            [True, False, True]
        ]
        self.assertEqual(solution(input), 4)

    def test_2(self):
        input = [
            [True, False, True, False, False, True, True, True],
            [True, False, True, False, False, False, True, False],
            [True, True, True, False, False, False, True, False],
            [True, False, True, False, False, False, True, False],
            [True, False, True, False, False, True, True, True]
        ]
        self.assertEqual(solution(input), 254)

    def test_3(self):
        input = [
            [True, True, False, True, False, True, False, True, True, False],
            [True, True, False, False, False, False, True, True, True, False],
            [True, True, False, False, False, False, False, False, False, True],
            [False, True, False, False, False, False, True, True, False, False]
        ]
        self.assertEqual(solution(input), 11567)


if __name__ == '__main__':
    unittest.main()
