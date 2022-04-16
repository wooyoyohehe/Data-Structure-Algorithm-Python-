class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        s = bin(n)
        left = 2
        right = 3
        while right < len(s):
            if s[right] == "1":
                ans = max(ans, right-left)
                left = right
                right += 1
            else:
                right += 1
        return ans
        