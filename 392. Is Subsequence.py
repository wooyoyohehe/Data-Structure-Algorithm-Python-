class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        p1 = p2 = 0
        while p2 < len(t):
            if s[p1] == t[p2]:
                if p1 == len(s)-1:
                    return True
                p1 += 1
            p2 += 1
        return False