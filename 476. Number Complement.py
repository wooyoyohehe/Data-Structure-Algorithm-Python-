class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        s = bin(num)[2:]
        for i in range(len(s)):
            if s[i] == "0":
                ans += 2 ** (len(s)-i-1)
        return ans
                