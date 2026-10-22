import unittest
from pattern_maker import make_pattern


class TestPattern(unittest.TestCase):
    def test_size(self):
        rows = make_pattern("stripes", 8)
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(len(r) == 8 for r in rows))

    def test_checker(self):
        rows = make_pattern("checker", 4)
        self.assertEqual(rows[0][0], "#")
        self.assertEqual(rows[0][1], " ")


if __name__ == "__main__":
    unittest.main()