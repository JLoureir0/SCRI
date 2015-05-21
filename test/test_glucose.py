import unittest
import pyversion.glucose as glucose

class GlucoseTest(unittest.TestCase):
    def test_blood_glucose_range(self):
        self.assertRaises(ValueError, glucose.blood_glucose, 0.9)
        self.assertRaises(ValueError, glucose.blood_glucose, 5.1)

    def test_blood_glucose_function(self):
        self.assertEqual(0.69121, glucose.blood_glucose(1.12345))
        self.assertEqual(3.88247, glucose.blood_glucose(2.23456))
        self.assertEqual(8.0931, glucose.blood_glucose(3.34567))
        self.assertEqual(17.02425, glucose.blood_glucose(4.57653))
        self.assertEqual(16.85495, glucose.blood_glucose(4.56224))
