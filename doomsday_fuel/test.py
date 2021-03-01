import unittest
from solution import solution


class TestDoomsdayFuel(unittest.TestCase):
    def test_1(self):
        input = [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        output = [7, 6, 8, 21]
        self.assertEqual(solution(input), output)

    def test_2(self):
        input = [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        output = [0, 3, 2, 9, 14]
        self.assertEqual(solution(input), output)

    def test_3(self):
        input = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        output = [1, 1]
        self.assertEqual(solution(input), output)


if __name__ == '__main__':
    unittest.main()
