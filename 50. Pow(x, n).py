class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if n == 0:
                return 1.0
            half = helper(x, n//2)
            if n%2 == 0:
                ans = half*half
            else:
                ans = half*half*x
            return ans
        if n >= 0:
            return helper(x,n)
        else:
            n = -n
            return 1/helper(x,n)