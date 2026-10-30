import unittest
from app.recommendations import analyze

class RecommendationTests(unittest.TestCase):
    def test_warns_when_memory_is_very_high(self):
        result = analyze({"cpu": {}, "memory": {"used_percent": 95}, "disks": {}})
        self.assertTrue(any(item["area"] == "RAM" and item["level"] == "warning" for item in result))

    def test_reports_low_free_disk_space(self):
        report = {
            "cpu": {},
            "memory": {},
            "disks": {"C:": {"free_gb": 5, "total_gb": 100}}
        }
        result = analyze(report)
        self.assertTrue(any(item["area"] == "Almacenamiento" for item in result))

if __name__ == "__main__":
    unittest.main()
