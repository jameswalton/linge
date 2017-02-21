import unittest
from vector import Vector

class VectorTest(unittest.TestCase):
    def test_plus(self):
        v = Vector([8.218, -9.341])
        new_vector = v.plus([-1.129, 2.111])
        self.assertEqual(new_vector, Vector([7.089, -7.229999999999999]))

    def test_minus(self):
        v = Vector([7.119, 8.215])
        new_vector = v.minus([-8.223, 0.878])
        self.assertEqual(new_vector, Vector([15.342, 7.337]))

    def test_times_scalar(self):
        v = Vector([1.671, -1.012, -0.318])
        new_vector = v.times_scalar(7.41)
        self.assertEqual(new_vector, Vector([12.38211, -7.49892, -2.35638]))

    def test_magnitude_2d(self):
        v = Vector([-0.221, 7.437])
        magnitude = v.magnitude()
        self.assertEqual(magnitude, 7.440282924728065)

    def test_magnitude_3d(self):
        v = Vector([8.813, -1.331, -6.247])
        magnitude = v.magnitude()
        self.assertEqual(magnitude, 10.884187567292289)

    def test_unit_2d(self):
        v = Vector([5.581, -2.136])
        unit = v.unit()
        self.assertEqual(unit, Vector([0.9339352140866403, -0.35744232526233]))

    def test_unit_3d(self):
        v = Vector([1.996, 3.108, -4.554])
        unit = v.unit()
        self.assertEqual(unit, Vector([0.3404012959433014, 0.5300437012984873, -0.7766470449528029]))
