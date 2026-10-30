import unittest

from app.thermal import _classify, _load_sensor_data, thermal_recommendations


class ThermalTests(unittest.TestCase):
    def test_sensor_json_object(self):
        sensors = _load_sensor_data('{"Name":"CPU Package","Value":72.5}')
        self.assertEqual(len(sensors), 1)
        self.assertEqual(sensors[0]["celsius"], 72.5)

    def test_cpu_high_temperature(self):
        result = _classify({"name": "CPU Package", "celsius": 96})
        self.assertEqual(result["component"], "CPU")
        self.assertEqual(result["level"], "alto")

    def test_gpu_warning_temperature(self):
        result = _classify({"name": "GPU Core", "celsius": 87})
        self.assertEqual(result["component"], "GPU")
        self.assertEqual(result["level"], "precaucion")

    def test_no_data_advice(self):
        advice = thermal_recommendations({"status": "sin_datos"})
        self.assertTrue(any("No hay lecturas" in item for item in advice))


if __name__ == "__main__":
    unittest.main()
