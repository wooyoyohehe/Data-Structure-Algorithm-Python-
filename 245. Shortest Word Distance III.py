class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dic = dict()
        dic[word1] = []
        dic[word2] = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                dic[wordsDict[i]].append(i)
        i, j, ans = 0, 0, float("inf")
        while i < len(dic[word1]) and j < len(dic[word2]):
            w1 = dic[word1][i]
            w2 = dic[word2][j]
            if w1 > w2:
                j+=1
                ans = min(ans, w1-w2)
            else:
                i += 1
                if w1 != w2:
                    ans = min(ans, w2-w1)
        return ans
        