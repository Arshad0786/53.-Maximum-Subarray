import unittest
from MaximumSubarray import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(temp.maxSubArray(self.input), 6)


if __name__ == "__main__":
    unittest.main()
