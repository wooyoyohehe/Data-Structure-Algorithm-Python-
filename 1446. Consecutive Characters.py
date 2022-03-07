class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 1
        ans = 1
        while right < len(s):
            while right < len(s) and s[left] == s[right]:
                right += 1
            ans = max(ans, right-left)
            left = right
            right += 1
        return ans
        