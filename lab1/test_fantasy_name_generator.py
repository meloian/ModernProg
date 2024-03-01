import unittest
from fantasy_name_generator import generate_name

class TestFantasyNameGenerator(unittest.TestCase):
    def test_generate_name(self):
        name = generate_name()
        self.assertTrue(isinstance(name, str) and len(name) > 0)

if __name__ == '__main__':
    unittest.main() 