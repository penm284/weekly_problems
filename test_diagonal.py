import unittest
import diagonal_sum

matrix1 = [[0 + x for x in range(5)] for y in range(5)]
matrix2 =[[0 + x for x in range(10)] for y in range(10)]
matrix3 =[[0 + x for x in range(8)] for y in range(8)]
matrix4 =[[0 + x for x in range(9)] for y in range(9)]
matrix5 =[[0 + x for x in range(3)] for y in range(3)]
matrix6 =[[0 + x for x in range(50)] for y in range(50)]
matrix7 =[[0 + x for x in range(100)] for y in range(100)]
matrix8 =[[0 + x for x in range(800)] for y in range(800)]

class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix1), 10, "output should be 10")

    def test_mild(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix2), 45, "output should be 45" )

    def test_hard(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix3), 28, "output should be 28" )

    def test_spicy(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix4), 36, "output should be 36" )

    def test_easy(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix5), 3, "output should be 3" )

    def test_hot(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix6), 1225, "output should be 1225" )

    def test_burning(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix7), 4950, "output should be 4950" )

    def test_burning_hot(self):
        self.assertEqual(diagonal_sum.diagonal_sum(matrix8), 319600, "output should be 319600" )



if __name__ == '__main__':
    unittest.main()
