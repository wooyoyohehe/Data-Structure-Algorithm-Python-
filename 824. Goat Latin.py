class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] in "aeiouAEIOU":
                new_word = words[i]+"ma"+"a"*(i+1)
            else:
                new_word = words[i][1:]+words[i][0]+"ma"+"a"*(i+1)
            words[i] = new_word
        return " ".join(words)