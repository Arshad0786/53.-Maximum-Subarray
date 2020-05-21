class Solution:
    def maxSubArray(self, nums):
        globalMax = -9223372036854775806  # smallest integer posible
        localMax = 0
        for i in range(len(nums)):
            localMax = max(nums[i], nums[i] + localMax)
            if localMax > globalMax:
                globalMax = localMax
        return globalMax
