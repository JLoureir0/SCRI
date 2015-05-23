import unittest
import pyversion.insuline as insuline

class InsulineTest(unittest.TestCase):
    def test_calculate_trends(self):
        self.assertEqual([0, 1, 0.5, 'FAIL', 0.66667, 0.5, 0.6, 0, 0.2, 'FAIL', 0.6, 0.6, 0.4, 0.6, 0.2, -0.32], insuline.calculate_trends([1, 2, 2, 'FAIL', 3, 3, 4, 2, 3, 'FAIL', 6, 6, 6, 5, 4, 4.4]))

    def test_calculate_dosages(self):
        self.assertEqual([0, 7], insuline.calculate_dosages([[1, 2], [2, '--'], [3, 3], [4, 2], [3, '--'], [6, 6], [6, 5], [4, 4.4]]))
