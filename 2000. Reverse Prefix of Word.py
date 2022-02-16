class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        i = 0
        while i < len(word) and word[i] != ch:
            i+=1
        if i == len(word):
            return word
        return word[:i+1][::-1]+word[i+1:]