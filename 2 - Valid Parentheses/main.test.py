import unittest
from main import Solution


class TestSolution(unittest.TestCase):
    def test_valid_parentheses(self):
        s = Solution()
        self.assertEqual(s.isValid("()"), True)
        self.assertEqual(s.isValid("()[]{}"), True)
        self.assertEqual(s.isValid("(]"), False)
        self.assertEqual(s.isValid("([)]"), False)
        self.assertEqual(s.isValid("{[]}"), True)


if __name__ == "__main__":
    unittest.main()
