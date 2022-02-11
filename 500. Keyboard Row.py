class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        ans =[]
        for word in words:
            if word[0] in rows[0]:
                row = rows[0]
            elif word[0] in rows[1]:
                row = rows[1]
            else:
                row = rows[2]
            flag = True
            for digit in word:
                if digit not in row:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans