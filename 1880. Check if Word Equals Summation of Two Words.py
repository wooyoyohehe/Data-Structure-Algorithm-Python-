class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        num1, num2,num3 = 0,0,0
        for letter in firstWord:
            num1 = num1*10 + ord(letter) - ord("a")
        for letter in secondWord:
            num2 = num2*10 + ord(letter) - ord("a")
        for letter in targetWord:
            num3 = num3*10 + ord(letter) - ord("a")
        return num3 == num1 + num2
        