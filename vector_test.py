import unittest
from vector import Vector

class VectorTest(unittest.TestCase):
    def test_plus(self):
        v = Vector([8.218, -9.341])
        self.assertEqual(v.plus([-1.129, 2.111]), [7.089, -7.229999999999999])

    def test_minus(self):
        v = Vector([7.119, 8.215])
        self.assertEqual(v.minus([-8.223, 0.878]), [15.342, 7.337])

    def test_scalar_multiply(self):
        v = Vector([1.671, -1.012, -0.318])
        self.assertEqual(v.scalar_multiply(7.41), [12.38211, -7.49892, -2.35638])
