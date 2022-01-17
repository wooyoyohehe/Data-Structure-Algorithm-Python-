class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        dic = {}

        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != s[i]:
                        return False
            elif s[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = s[i]
        return True