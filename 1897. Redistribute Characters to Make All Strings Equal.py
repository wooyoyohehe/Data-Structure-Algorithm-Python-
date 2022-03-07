class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        dic = {}
        for word in words:
            for letter in word:
                if letter not in dic:
                    dic[letter] = 1
                else:
                    dic[letter] += 1
        for key in dic:
            if dic[key] % len(words) != 0:
                return False
        return True
        