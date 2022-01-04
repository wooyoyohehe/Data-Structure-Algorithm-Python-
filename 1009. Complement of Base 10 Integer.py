class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        ans = 0
        for i in range(2, len(s)):
            if s[i] == '0':
                ans += 2 ** (len(s)-i-1)
        return ans
                
        