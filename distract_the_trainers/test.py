import unittest
from solution import solution


class TestDistractTheTrainers(unittest.TestCase):
    def test_1(self):
        input = [1, 1]
        self.assertEqual(solution(input), 2)

    def test_2(self):
        input = [1, 7, 3, 21, 13, 19]
        self.assertEqual(solution(input), 0)

    def test_3(self):
        input = [1, 2, 8, 7, 6, 45, 12]
        self.assertEqual(solution(input), 1)

    def test_4(self):
        input = [1, 2, 8, 7, 6, 45, 12, 258, 234, 11, 157]
        self.assertEqual(solution(input), 1)


if __name__ == '__main__':
    unittest.main()
