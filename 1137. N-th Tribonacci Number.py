class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        a = 0
        b = c = 1
        for i in range(n-2):
            temp = c
            c = a+b+c
            a = b
            b = temp
        return c