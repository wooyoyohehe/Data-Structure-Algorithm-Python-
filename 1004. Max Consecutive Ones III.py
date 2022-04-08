class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [1,1,1,0,0]
        #  |       |
        left = 0
        right = 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
                if k < 0:
                    while left < right and nums[left] == 1:
                        left += 1
                    k += 1
                    left += 1
                else:
                    ans = max(ans, right-left+1)
                right += 1
            else:
                ans = max(ans, right-left+1)
                right += 1
        return ans
                