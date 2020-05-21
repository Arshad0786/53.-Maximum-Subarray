import unittest
from MaximumSubarray import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(temp.maxSubArray(self.input), 6)

    def test_all_1(self):
        temp = Solution()
        self.input = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(temp.maxSubArray(self.input), 20)

    def test_all_0(self):
        temp = Solution()
        self.input = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(temp.maxSubArray(self.input), 0)

    def test_one_large_negative(self):
        temp = Solution()
        self.input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-100000]
        self.assertEqual(temp.maxSubArray(self.input), 120)

if __name__ == "__main__":
    unittest.main()
