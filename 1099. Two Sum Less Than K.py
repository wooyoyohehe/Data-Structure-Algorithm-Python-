class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = -1
        while left < right:
            if nums[left] + nums[right] < k:
                ans = max(ans, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return ans
        