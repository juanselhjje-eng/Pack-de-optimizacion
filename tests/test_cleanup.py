import unittest
from app.cleanup import get_temp_cleanup_preview

class CleanupTests(unittest.TestCase):
    def test_preview_does_not_delete(self):
        result = get_temp_cleanup_preview()
        self.assertFalse(result["deleted"])
        self.assertIn("directory", result)

if __name__ == "__main__":
    unittest.main()
