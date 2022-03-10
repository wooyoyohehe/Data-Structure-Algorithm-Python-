class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text = text.split(" ")
        ans = 0
        for i in range(len(text)):
            flag = True
            for letter in brokenLetters:
                if letter in text[i]:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans