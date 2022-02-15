class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            if s[i] not in "aeiou":
                ans += s[i]
        return ans