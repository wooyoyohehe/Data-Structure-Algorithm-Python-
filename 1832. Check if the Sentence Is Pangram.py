class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = set()
        for s in sentence:
            letters.add(s)
        return len(letters) == 26
        