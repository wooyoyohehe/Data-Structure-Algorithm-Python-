class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1, w2 = [], []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1.append(i)
            elif wordsDict[i] == word2:
                w2.append(i)
        ans = float("inf")
        for i in w1:
            for j in w2:
                ans = min(ans, abs(i-j))
        return ans