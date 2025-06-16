# test_compute_stats.py
import unittest
from lab_task import compute_stats

class TestStats(unittest.TestCase):
    def test_normal_data(self):
        result = compute_stats([10, 20, 30])
        self.assertEqual(result['total'], 3)
        self.assertEqual(result['sum'], 60)
        self.assertEqual(result['average'], 20)
        self.assertEqual(result['min'], 10)
        self.assertEqual(result['max'], 30)

    def test_empty_data(self):
        result = compute_stats([])
        self.assertEqual(result['total'], 0)
        self.assertEqual(result['sum'], 0)
        self.assertEqual(result['average'], 0)
        self.assertIsNone(result['min'])
        self.assertIsNone(result['max'])

if __name__== '_main_':
    unittest.main()