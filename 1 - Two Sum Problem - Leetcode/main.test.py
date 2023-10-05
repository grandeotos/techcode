import unittest
from main import Solution


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(s.twoSum([3, 3], 6), [0, 1])
        self.assertEqual(s.twoSum([1, 2, 3, 4, 5], 9), [3, 4])
        self.assertEqual(s.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])


if __name__ == "__main__":
    unittest.main()
