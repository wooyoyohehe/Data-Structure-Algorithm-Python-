class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        ans = ""
        count = 0
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        if i == len(word1):
            ans += word2[j:]
        else:
            ans += word1[i:]
        return ans
        