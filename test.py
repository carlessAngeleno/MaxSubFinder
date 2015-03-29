import unittest

from MaxSubFinder import findSubsequence


class TestSubsFinder(unittest.TestCase):

    def test_1(self):
        arr = [5, -1, -3, 2, 4, -3]
        self.assertEqual(findSubsequence(arr), 7)

    def test_empty_array(self):
        arr = []
        self.assertTrue(findSubsequence(arr) == None)

    def test_validation(self):
        arr = ['a', 'b', 'sdfs']
        self.assertTrue(findSubsequence(arr) == None)

    def test_all_zeros(self):
        arr = [0, 0, 0]
        self.assertEqual(findSubsequence(arr), 0)

    def test_all_negatives(self):
        arr = [-1, -4, -3]
        self.assertEqual(findSubsequence(arr), -1)

    def test_all_positivies(self):
        arr = [2, 3, 54]
        self.assertEqual(findSubsequence(arr), 59)


if __name__ == '__main__':
    unittest.main()