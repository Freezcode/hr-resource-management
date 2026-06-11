import unittest

from hr_metrics import evaluate_hr_metrics


class TestHRMetrics(unittest.TestCase):
    def test_returns_excellent_when_scores_are_high(self):
        result = evaluate_hr_metrics(90, 88, 87)
        self.assertEqual(result["rating"], "Excellent")
        self.assertEqual(result["focus_areas"], ["Maintain current standards"])

    def test_flags_low_areas(self):
        result = evaluate_hr_metrics(65, 80, 60)
        self.assertEqual(result["rating"], "Average")
        self.assertEqual(result["focus_areas"], ["Productivity", "Work environment"])

    def test_rejects_invalid_scores(self):
        with self.assertRaises(ValueError):
            evaluate_hr_metrics(-1, 80, 80)


if __name__ == "__main__":
    unittest.main()
