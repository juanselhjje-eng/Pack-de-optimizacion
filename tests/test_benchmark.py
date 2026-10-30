import unittest
from app.benchmark import run_quick_benchmark

class BenchmarkTests(unittest.TestCase):
    def test_benchmark_returns_metrics(self):
        result = run_quick_benchmark()
        self.assertIn("cpu_hash_test_seconds", result)
        self.assertGreaterEqual(result["cpu_hash_test_seconds"], 0)

if __name__ == "__main__":
    unittest.main()
