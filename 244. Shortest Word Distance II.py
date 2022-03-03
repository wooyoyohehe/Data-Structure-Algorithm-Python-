class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.dic = dict()
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.dic:
                self.dic[wordsDict[i]] = [i]
            else:
                self.dic[wordsDict[i]].append(i)
        
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indice1 = self.dic[word1]
        indice2 = self.dic[word2]
        ans = float("inf")
        i = 0
        j = 0
        ans = float("inf")
        while i < len(indice1) and j < len(indice2):
            cur_diff = abs(indice1[i]-indice2[j])
            if cur_diff <= ans:
                ans = cur_diff
            if indice1[i] > indice2[j]:
                j += 1
            else:
                i += 1
        return ans
            
                
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)