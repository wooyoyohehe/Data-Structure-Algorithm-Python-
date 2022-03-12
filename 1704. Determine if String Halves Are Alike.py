class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        for i in range(len(s)/2):
            if s[i] in "aeiouAEIOU":
                count += 1
        for i in range(len(s)/2, len(s)):
            if s[i] in "aeiouAEIOU":
                count -= 1
        return count == 0
        