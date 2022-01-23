class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = 1
        left_max = right_max = nums[0]
        for i in range(len(nums)):
            left *= nums[i]
            right *= nums[-i-1]
            left_max = max(left, left_max)
            right_max = max(right, right_max)
            if nums[i] == 0:
                left = 1
            if nums[-i-1] == 0:
                right = 1
        return max(left_max,right_max)