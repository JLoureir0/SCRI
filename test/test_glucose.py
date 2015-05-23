import unittest
import pyversion.glucose as glucose

class GlucoseTest(unittest.TestCase):
    def test_blood_glucose_function(self):
        self.assertEqual(0.69121, glucose.blood_glucose(1.12345))
        self.assertEqual(3.88247, glucose.blood_glucose(2.23456))
        self.assertEqual(8.0931, glucose.blood_glucose(3.34567))
        self.assertEqual(17.02425, glucose.blood_glucose(4.57653))
        self.assertEqual(16.85495, glucose.blood_glucose(4.56224))

    def test_glucose_variation_function(self):
        self.assertEqual(2.68741, glucose.glucose_variation(1.12345))
        self.assertEqual(3.16969, glucose.glucose_variation(2.23456))
        self.assertEqual(4.68153, glucose.glucose_variation(3.34567))
        self.assertEqual(11.94570, glucose.glucose_variation(4.57653))
        self.assertEqual(11.75056, glucose.glucose_variation(4.56224))

    def test_glucose_variation_variation_function(self):
        self.assertEqual(0.12616, glucose.glucose_variation_variation(1.12345))
        self.assertEqual(0.75920, glucose.glucose_variation_variation(2.23456))
        self.assertEqual(2.28517, glucose.glucose_variation_variation(3.34567))
        self.assertEqual(13.85034, glucose.glucose_variation_variation(4.57653))
        self.assertEqual(13.46412, glucose.glucose_variation_variation(4.56224))

    def test_parse_reading(self):
        self.assertEqual([1.23456, 1.23456, 'FAIL', 2], glucose.parse_reading([['--', 1.23456],[1.23456, '--'],['--', '--'],[3, 1]]))

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

    def test_reading_out_of_sync(self):
        self.assertRaises(ValueError, glucose.reading_out_of_sync, [[1.1, 2.1], [1.2, 2.2], [1.3, 2.3]])
        self.assertEquals([[2.1, 2.1], [2.2, 2.2], [2.3, 2.3]], glucose.reading_out_of_sync([[2.1, 2.1], [2.2, 2.2], [2.3, 2.3]]))

    def test_glucose_values(self):
        self.assertEqual(['FAIL'], glucose.glucose_values([[0, 0],[0, 0], [0, 0]]))
        self.assertEqual([0.36019], glucose.glucose_values([[1, 1],[0, 1], [0, 1]]))
        self.assertRaises(ValueError, glucose.glucose_values, [[1.1, 2.1], [1.2, 2.2], [1.3, 2.3]])

    def test_glucose_for_dosage(self):
        self.assertEqual([0.36019], glucose.glucose_for_dosage([0.36019, 0.36019, 'FAIL']))
        self.assertEqual([0.36019], glucose.glucose_for_dosage([0.36019, 'FAIL', 0.36019]))
        self.assertEqual([0.36019], glucose.glucose_for_dosage(['FAIL', 0.36019, 0.36019]))
        self.assertEqual([0.36019], glucose.glucose_for_dosage(['FAIL', 0.36019, 'FAIL']))
        self.assertEqual([0.36019], glucose.glucose_for_dosage(['FAIL', 'FAIL', 0.36019]))
        self.assertEqual([0.36019], glucose.glucose_for_dosage([0.36019, 'FAIL', 'FAIL']))
        self.assertEqual(['FAIL'], glucose.glucose_for_dosage(['FAIL', 'FAIL', 'FAIL']))
        self.assertEqual([2], glucose.glucose_for_dosage([3, 3, 2]))
        self.assertEqual([2], glucose.glucose_for_dosage([3, 3, 2, 3]))
        self.assertEqual([2, 3], glucose.glucose_for_dosage([3, 3, 2, 3, 2, 3]))
