class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum_ = 0
        for i in range(0, len(nums),2):
            sum_ += nums[i]
        return sum_