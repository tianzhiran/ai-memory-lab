import unittest

from main import clean_memory

class TestMemory(unittest.TestCase):

    def test_remove_spaces(self):
        self.assertEqual(
            clean_memory("   Hello AI   "),
            "hello ai"
        )

    def test_lowercase(self):
        self.assertEqual(
            clean_memory("PYTHON is FUN"),
            "python is fun"
        )

    def test_empty_input(self):
        self.assertEqual(
            clean_memory("   "),
            ""
        )

if __name__ == "__main__":
    unittest.main()