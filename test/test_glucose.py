import unittest
import pyversion.glucose as glucose

class GlucoseTest(unittest.TestCase):
    def test_blood_glucose_function(self):
        self.assertEqual(0.69121, glucose.blood_glucose(1.12345))
        self.assertEqual(3.88247, glucose.blood_glucose(2.23456))
        self.assertEqual(8.0931, glucose.blood_glucose(3.34567))
        self.assertEqual(17.02425, glucose.blood_glucose(4.57653))
        self.assertEqual(16.85495, glucose.blood_glucose(4.56224))

    def test_parse_reading(self):
        self.assertEqual([1.23456, 1.23456, '--', 2], glucose.parse_reading([['--', 1.23456],[1.23456, '--'],['--', '--'],[3, 1]]))

    def test_reading_out_of_range(self):
        self.assertEqual([['--', 1], [5, '--'], [1, 5], ['--', '--']], glucose.reading_out_of_range([[0, 1], [5, 6], [1, 5], ['--', '--']]))

    def test_reading_stuck_at(self):
        self.assertEqual([[0, 1], [0, 2], ['--', 3]], glucose.reading_stuck_at([[0, 1], [0, 2], [0, 3]]))
        self.assertEqual([[0, 1], [0, 2], ['--', 3], [1, 2]], glucose.reading_stuck_at([[0, 1], [0, 2], [0, 3], [1, 2]]))
        self.assertEqual([[1, 2], [0, 1], [0, 2], ['--', 3]], glucose.reading_stuck_at([[1, 2], [0, 1], [0, 2], [0, 3]]))
        self.assertEqual([[0, 2], [0, 1], ['--', 2], ['--', 3]], glucose.reading_stuck_at([[0, 2], [0, 1], ['--', 2], [0, 3]]))
        self.assertEqual([[1, 2], [0, 1], [1, 2], [0, 3]], glucose.reading_stuck_at([[1, 2], [0, 1], [1, 2], [0, 3]]))

    def test_reading_random(self):
        self.assertEqual([[1, 1], ['--', '--'], [1, '--']], glucose.reading_random([[1, 1], ['--', 3], [1, 2]]))
        self.assertEqual([[1, 1], [1.3, '--'], [1.3, '--']], glucose.reading_random([[1, 1], [1.3, 3], [1.3, 2]]))
