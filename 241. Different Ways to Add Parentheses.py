class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        left, right = 0, 0
        ans = len(nums) + 1
        while right < len(nums):
            if sum(nums[left:right+1]) >= target:
                ans = min(ans, right-left+1)
                temp_sum = sum(nums[left:right+1])
                while temp_sum - nums[left] >= target:
                    temp_sum -= nums[left]
                    left += 1
                ans = min(ans, right-left+1)
            right += 1
        return ans