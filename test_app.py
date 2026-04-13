import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        result = greet("Anay")
        self.assertIn("Anay", result)
        self.assertIn("AIIDI 2004", result)

    def test_farewell(self):
        result = farewell("Anay")
        self.assertIn("Anay", result)

if __name__ == "__main__":
    unittest.main()