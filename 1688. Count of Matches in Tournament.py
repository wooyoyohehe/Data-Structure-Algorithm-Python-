class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 1:
            ans += n // 2
            n = (n+1)//2
        return ans