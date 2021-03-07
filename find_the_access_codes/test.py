import unittest
from solution import solution


class TestFindTheAccessCodes(unittest.TestCase):
    def test_1(self):
        input = [1, 1, 1]
        output = 1
        self.assertEqual(solution(input), output)

    def test_2(self):
        input = [1, 2, 3, 4, 5, 6]
        output = 3
        self.assertEqual(solution(input), output)

    def test_3(self):
        input = [1, 2]
        output = 0
        self.assertEqual(solution(input), output)

    def test4(self):
        input = range(1, 2001)
        output = 40888
        self.assertEqual(solution(input), output)


if __name__ == '__main__':
    unittest.main()
