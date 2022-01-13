class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        left = right = 1
        for i in range(len(nums)):
            result[i] *= left
            left *= nums[i]
            result[len(nums)-i-1] *= right
            right *= nums[len(nums)-i-1]

        return result