class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        left = 0
        right = 1
        ans = len(nums)
        for left in range(len(nums)):
            right = left + 1
            while right < len(nums) and nums[left] == nums[right]:
                if right - left == 2:
                    nums.pop(right)
                    ans -= 1
                    continue
                right += 1
        return ans