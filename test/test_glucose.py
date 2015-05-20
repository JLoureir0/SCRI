import unittest
import pyversion.glucose as glucose

class GlucoseTest(unittest.TestCase):
    def test_blood_glucose(self):
        self.assertEqual(-2.64411, glucose.blood_glucose(0.03433))
        self.assertEqual(-2.63052, glucose.blood_glucose(0.03624))
        self.assertEqual(-1.71946, glucose.blood_glucose(0.25675))
        self.assertEqual(-1.70506, glucose.blood_glucose(0.26123))
        self.assertEqual(17.02425, glucose.blood_glucose(4.57653))
        self.assertEqual(16.85495, glucose.blood_glucose(4.56224))
