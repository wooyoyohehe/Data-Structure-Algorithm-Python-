class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for ss in s:
            if ss not in dic:
                dic[ss] = 1
            else:
                dic[ss] += 1
        num = dic[s[0]]
        for key in dic:
            if dic[key] != num:
                return False
        return True