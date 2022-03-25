class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        cur_smallest = 1
        for num in nums:
            cur += num
            if cur < 1:
                cur_smallest = max(cur_smallest, 1-cur)
        return cur_smallest
            
        