class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1.0/x
            n = -n
        cur = x
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans*cur
            cur *= cur
            n /= 2
        return ans