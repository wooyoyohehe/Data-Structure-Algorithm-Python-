class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s = sum_t = 0
        for i in range(len(s)):
            sum_s += ord(s[i])
            sum_t += ord(t[i])
        sum_t += ord(t[-1])
        return chr(sum_t-sum_s)