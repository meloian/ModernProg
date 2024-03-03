import unittest
from fantasy_name_generator import generate_name, generate_title_name, generate_biography, generate_characteristics, calculate_magic_power, generate_race

class TestFantasyNameGenerator(unittest.TestCase):
    def test_generate_name(self):
        name = generate_name()
        self.assertTrue(isinstance(name, str) and len(name) > 0)

    def test_generate_title_name(self):
        title_name = generate_title_name()
        self.assertTrue(isinstance(title_name, str) and len(title_name) > 0)
        self.assertIn(title_name.split()[0], ["Lord", "Sir", "Magister", "Warrior", "Archmage", "Ranger", "Assassin", "Bard"])

    def test_generate_race(self):
        race = generate_race()
        self.assertIn(race, ["Elf", "Dwarf", "Human", "Orc", "Tiefling", "Halfling", "Gnome", "Dragonborn"])

    def test_generate_biography(self):
        bio = generate_biography()
        self.assertTrue(isinstance(bio, str) and len(bio) > 0)
        # check if the biography includes a race
        self.assertTrue(any(race in bio for race in ["Elf", "Dwarf", "Human", "Orc", "Tiefling", "Halfling", "Gnome", "Dragonborn"]))

    def test_generate_characteristics(self):
        age, courses_taken, enemies_defeated = generate_characteristics()
        self.assertTrue(isinstance(age, int) and 18 <= age <= 100)
        self.assertTrue(isinstance(courses_taken, int) and 1 <= courses_taken <= 10)
        self.assertTrue(isinstance(enemies_defeated, int) and 0 <= enemies_defeated <= 50)

    def test_calculate_magic_power(self):
        self.assertEqual(calculate_magic_power(30, 5, 10), 16)
        self.assertEqual(calculate_magic_power(50, 2, 20), 12)
        self.assertNotEqual(calculate_magic_power(25, 3, 5), 0)

if __name__ == '__main__':
    unittest.main()