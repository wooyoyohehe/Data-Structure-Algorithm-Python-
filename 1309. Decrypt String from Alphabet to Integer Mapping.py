class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        ans = ""
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                ans += chr(int(s[i:i+2]) + ord("a") -1)
                i += 3
            else:
                ans += chr(int(s[i]) + ord("a") - 1)
                i += 1
        return ans