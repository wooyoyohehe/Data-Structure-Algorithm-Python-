class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        cur = 1
        ans = 0
        while right < len(nums):
            cur *= nums[right]
            while left <= right and cur >= k:
                cur /= nums[left]
                left += 1
            if cur < k:
                ans += right - left + 1
            right += 1
        return ans