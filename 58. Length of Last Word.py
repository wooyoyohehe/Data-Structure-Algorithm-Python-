class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        i = len(s)-1
        while s[i] == ' ':
            i-=1
        ans = 0
        while s[i] != ' ' and i>=0:
            ans+=1
            i-=1
        return ans