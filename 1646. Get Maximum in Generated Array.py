class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        nums = [0]*(n+1)
        nums[0] = 0
        nums[1] = 1
        for i in range(n+1):
            if i%2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[(i-1)//2]+nums[(i-1)//2+1]
        return max(nums)