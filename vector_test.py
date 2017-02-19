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
