import unittest
from solution import solution


class TestRunningWithBunnies(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            solution(
                [
                    [0, 2, 2, 2, -1],
                    [9, 0, 2, 2, -1],
                    [9, 3, 0, 2, -1],
                    [9, 3, 2, 0, -1],
                    [9, 3, 2, 2, 0]
                ],
                1
            ),
            [1, 2]
        )

    def test_2(self):
        self.assertEqual(
            solution(
                [
                    [0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0]
                ],
                3
            ),
            [0, 1]
        )


if __name__ == '__main__':
    unittest.main()
