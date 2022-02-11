class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        ans = 0
        while i < len(nums):
            if nums[i] == 0:
                i+= 1
            else:
                j = i
                while i < len(nums) and nums[i] == 1:
                    i+=1
                ans = max(ans, i-j)
        return ans