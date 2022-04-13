class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = {}
        letter = set()
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
                if t[i] in letter:
                    return False
                letter.add(t[i])
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True