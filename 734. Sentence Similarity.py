class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence2) != len(sentence1):
            return False
        dic = {}
        for word in sentence1:
            dic[word] = set()
            dic[word].add(word)
        for word in sentence2:
            dic[word] = set()
            dic[word].add(word)
        for pairs in similarPairs:
            if pairs[0] in dic and pairs[1] in dic:
                dic[pairs[0]].add(pairs[1])
                dic[pairs[1]].add(pairs[0])
        for i in range(len(sentence1)):
            if sentence2[i] not in dic[sentence1[i]]:
                return False
        return True