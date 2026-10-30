import unittest
from app.profiles import PROFILES

class ProfileTests(unittest.TestCase):
    def test_expected_profiles_exist(self):
        self.assertIn("General", PROFILES)
        self.assertIn("Programacion", PROFILES)
        self.assertIn("Gaming", PROFILES)

if __name__ == "__main__":
    unittest.main()
