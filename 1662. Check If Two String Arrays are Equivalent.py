class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s1 = ""
        s2 = ""
        for w in word1:
            s1 += w
        for w in word2:
            s2 += w
        return s1 == s2