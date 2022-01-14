class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while 1:
            if n % 2 == 0:
              n /= 2
            elif n % 3 == 0:
              n /= 3
            elif n % 5 == 0:
              n /= 5
            else:
              if n == 1:
                return True
              else:
                return False