class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        ans = 0
        for i in range(3, n+1):
            ans = a+b
            a = b
            b = ans
        return ans