class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        digits = []
        length = len(str(n))
        while n != 0:
            digits.append((n%10)**length)
            n = n // 10
        return sum(digits) == num