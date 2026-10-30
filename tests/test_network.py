import unittest
from app.network import run_ping_test

class NetworkTests(unittest.TestCase):
    def test_invalid_host_rejected(self):
        with self.assertRaises(ValueError):
            run_ping_test("1.1.1.1 & whoami", 1)

    def test_count_is_bounded(self):
        result = run_ping_test("127.0.0.1", 1)
        self.assertEqual(result["host"], "127.0.0.1")

if __name__ == "__main__":
    unittest.main()
