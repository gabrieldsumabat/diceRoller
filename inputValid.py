import re
import unittest


def inputValid(userInput):
    """Verifies user input as valid. Accepts strings. Returns True for valid input, False for invalid."""
    regex = "\d+[d,D]+\d+[+,-]\d+"
    if re.search(regex, userInput):
        return True
    else:
        return False


class TestValidMethod(unittest.TestCase):
    """Test cases to ensure edge cases."""

    def testFalse(self):
        self.assertFalse(inputValid("1dd+7"))
        self.assertFalse(inputValid("1e3+8"))

    def testTrue(self):
        self.assertTrue(inputValid("1d7+8"))
        self.assertTrue(inputValid("11d7+8"))
        self.assertTrue(inputValid("1d12+2"))
        self.assertTrue(inputValid("1d7+12"))


if __name__ == "__main__":
    unittest.main()
