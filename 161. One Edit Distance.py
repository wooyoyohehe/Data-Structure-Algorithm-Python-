class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s)-len(t)) >= 2 or s == t:
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if len(s) == len(t):
                    if s[i+1:] == t[j+1:]:
                        return True
                if len(s) > len(t):
                    if s[i+1:] == t[j:]:
                        return True
                else:
                    if s[i:] == t[j+1:]:
                        return True
                return False
        return True