class WordDictionary(object):

    def __init__(self):
        self.dic = {}
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word) not in self.dic:
            self.dic[len(word)] = set()
        self.dic[len(word)].add(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.dic:
            return False
        for w in self.dic[len(word)]:
            p1 = 0
            p2 = 0
            flag = 1
            for i in range(len(word)):
                if word[i] == "." or word[i] == w[i]:
                    p1 += 1
                    p2 += 1
                else:
                    flag = 0
                    break
            if flag == 1:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)