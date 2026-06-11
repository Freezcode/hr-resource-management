import unittest

from hr_metrics import evaluate_hr_metrics


class TestEvaluateHRMetrics(unittest.TestCase):
    def test_returns_excellent_when_scores_are_high(self):
        result = evaluate_hr_metrics(90, 88, 87)
        self.assertEqual(result["rating"], "Excellent")
        self.assertEqual(result["focus_areas"], ["Maintain current standards"])

    def test_identifies_focus_areas_for_low_scores(self):
        result = evaluate_hr_metrics(65, 80, 60)
        self.assertEqual(result["rating"], "Average")
        self.assertEqual(result["focus_areas"], ["Productivity", "Work Environment"])

    def test_threshold_boundary_for_focus_areas(self):
        result = evaluate_hr_metrics(70, 69.99, 70)
        self.assertEqual(result["focus_areas"], ["Work Climate"])

    def test_rejects_invalid_scores(self):
        with self.assertRaises(ValueError):
            evaluate_hr_metrics(-1, 80, 80)

        with self.assertRaises(ValueError):
            evaluate_hr_metrics(80, 101, 80)

        with self.assertRaises(ValueError):
            evaluate_hr_metrics(80, 80, 120)


if __name__ == "__main__":
    unittest.main()
