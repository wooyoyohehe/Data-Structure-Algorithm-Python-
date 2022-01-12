class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
        for hehe in a:
            if a[hehe] == 1:
                return hehe