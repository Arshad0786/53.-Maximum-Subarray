class Solution:
    def maxSubArray(self, nums):
        maxSum = int()
        for ScanSize in range(1, len(nums) + 1):
            for i in range(len(nums) - ScanSize + 1):

                if (ScanSize == 1) and (i == 0):
                    maxSum = self.SumOfPartArray(nums, i, i + ScanSize - 1)

                if self.SumOfPartArray(nums, i, i + ScanSize - 1) > maxSum:
                    maxSum = self.SumOfPartArray(nums, i, i + ScanSize - 1)

        return maxSum

    def SumOfPartArray(self, nums, start, end):
        sum = 0
        for i in range(end - start + 1):
            sum = sum + nums[start + i]
        return sum
