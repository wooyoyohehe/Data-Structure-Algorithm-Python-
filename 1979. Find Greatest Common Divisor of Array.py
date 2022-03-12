class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = min(nums)
        min_ = min(nums)
        max_ = max(nums)
        while ans > 1:
            if max_%ans == 0 and min_%ans == 0:
                return ans
            else:
                ans -= 1
        return 1