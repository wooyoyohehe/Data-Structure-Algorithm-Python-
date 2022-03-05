class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        dic = dict()
        for i in range(26):
            dic[keyboard[i]] = i
        ans = abs(dic[word[0]] - dic[keyboard[0]])
        for i in range(len(word)-1):
            ans += abs(dic[word[i]] - dic[word[i+1]])
        return ans
        