class Solution(object):
    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        right = 0
        while right < len(s):
            while right < len(s) and s[left] == s[right]:
                right += 1
            length = right - left
            ans += (1+length)*length/2
            left = right
        return ans